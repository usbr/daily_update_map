# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:26:04 2019

@author: buriona
"""

import re
import json
from os import path
import folium
import branca
import pandas as pd
# import geopandas as gpd
from shapely.geometry import Point
from datetime import datetime
from requests import get as r_get

STATIC_URL = f'https://www.usbr.gov/uc/water/hydrodata/assets'
NRCS_CHARTS_URL = 'https://nwcc-apps.sc.egov.usda.gov/awdb/basin-plots/POR'

def get_plotly_js():
    return f'{STATIC_URL}/plotly.js'

def get_favicon():
    return f'{STATIC_URL}/img/favicon.ico'

def get_bootstrap():
    return {
        'css': f'{STATIC_URL}/bootstrap/css/bootstrap.min.css',
        'js': f'{STATIC_URL}/bootstrap/js/bootstrap.bundle.js',
        'jquery': f'{STATIC_URL}/jquery.js',
        'popper': f'{STATIC_URL}/popper.js',
        'fa': f'{STATIC_URL}/font-awesome/css/font-awesome.min.css',
    }

def get_bor_seal(orient='default', grey=False):
    color = 'cmyk'
    if grey:
        color = 'grey'
    seal_dict = {
        'default': f'BofR-horiz-{color}.png',
        'shield': 'BofR-shield-cmyk.png',
        'vert': f'BofR-vert-{color}.png',
        'horz': f'BofR-horiz-{color}.png'
        }
    return f'{STATIC_URL}/img/{seal_dict[orient]}'

def get_bor_js():
    return [
        ('leaflet',
          f'{STATIC_URL}/js/leaflet/leaflet.js'),
        ('jquery',
          f'{STATIC_URL}/js/jquery/3.4.0/jquery.min.js'),
        ('bootstrap',
          f'{STATIC_URL}/js/bootstrap/3.2.0/js/bootstrap.min.js'),
        ('awesome_markers',
          f'{STATIC_URL}/js/leaflet/leaflet.awesome-markers.js'),  # noqa
        ]

def get_bor_css():
    return [
        ('leaflet_css',
          f'{STATIC_URL}/css/leaflet/leaflet.css'),
        ('bootstrap_css',
          f'{STATIC_URL}/css/bootstrap/3.2.0/css/bootstrap.min.css'),
        ('bootstrap_theme_css',
          f'{STATIC_URL}/css/bootstrap/3.2.0/css/bootstrap-theme.min.css'),  # noqa
        ('awesome_markers_font_css',
          f'{STATIC_URL}/css/font-awesome.min.css'),  # noqa
        ('awesome_markers_css',
          f'{STATIC_URL}/css/leaflet/leaflet.awesome-markers.css'),  # noqa
        ('awesome_rotate_css',
          f'{STATIC_URL}/css/leaflet/leaflet.awesome.rotate.css'),  # noqa
        ]

def get_default_js():
    bootstrap_dict = get_bootstrap()
    return [
        ('leaflet', 
         f'{STATIC_URL}/leaflet/js/leaflet.js'),
        ('jquery', 
         bootstrap_dict['jquery']),
        ('bootstrap', 
         bootstrap_dict['js']),
        ('awesome_markers', 
         f'{STATIC_URL}/leaflet-awesome-markers/leaflet.awesome-markers.min.js'),
        ('popper', 
         bootstrap_dict['popper']),
    ]

def get_default_css():
    bootstrap_dict = get_bootstrap()
    return [
        ('leaflet_css', 
         f'{STATIC_URL}/leaflet/css/leaflet.css'),
        ('bootstrap_css', 
         bootstrap_dict['css']),
        ('awesome_markers_font_css', 
          bootstrap_dict['fa']),
        ('awesome_markers_css', 
        f'{STATIC_URL}/leaflet-awesome-markers/leaflet.awesome-markers.css'),
        ('awesome_rotate_css', 
         f'{STATIC_URL}/leaflet-awesome-markers/leaflet.awesome.rotate.css'),
    ]

def get_fa_icon(obj_type='default', source='hdb'):
    if source.lower() == 'hdb':
        fa_dict = {
            'default': 'map-pin',
            1: 'sitemap',
            2: 'umbrella',
            3: 'arrow-down',
            4: 'exchange',
            5: 'plug',
            6: 'arrows-v',
            7: 'tint',
            8: 'snowflake-o',
            9: 'tachometer',
            10: 'cogs',
            11: 'arrows-h',
            12: 'rss',
            13: 'flask',
            14: 'table',
            15: 'info',
            20: 'exchange'
        }
    if source.lower() == 'awdb':
        fa_dict = {
            'default': 'map-pin',
            'SCAN': 'umbrella',
            'PRCP': 'umbrella',
            'BOR': 'tint',
            'SNTL': 'snowflake-o',
            'SNOW': 'snowflake-o',
            'SNTLT': 'snowflake-o',
            'USGS': 'tachometer',
            'MSNT': 'snowflake-o',
            'MPRC': 'umbrella'
        }
    fa_icon = fa_dict.get(obj_type, 'map-pin')
    return fa_icon

def get_icon_color(row, source='hdb'):
    if source.lower() == 'hdb':
        obj_owner = 'BOR'
        if not row.empty:
            if row['site_metadata.scs_id']:
                obj_owner = 'NRCS'
            if row['site_metadata.usgs_id']:
                obj_owner = 'USGS'
    if source.lower() == 'awdb':
        obj_owner = row
    color_dict = {
        'BOR': 'blue',
        'NRCS': 'red',
        'USGS': 'green',
        'COOP': 'gray',
        'SNOW': 'darkred',
        'PRCP': 'lightred',
        'SNTL': 'red',
        'SNTLT': 'lightred',
        'SCAN': 'lightred',
        'MSNT': 'orange',
        'MPRC': 'beige',
        
    }
    icon_color = color_dict.get(obj_owner, 'black')
    return icon_color

def add_optional_tilesets(folium_map):
    url_list = ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', 
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
                'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}', 
                'https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}']
    name_list = ['ESRI World Topo Map', 'ESRI World Street Map', 'ESRI Nat Geo', 'USGS Imagery Topo', 'USGS Topo', ]
    attr_list = ['Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community',
                 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
                 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
                 'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>', 
                 'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>']
    for url, name, attr in zip(url_list, name_list, attr_list):
      folium.TileLayer(
          tiles=url,
          name=name,
          attr=attr,
          subdomains='mytilesubdomain').add_to(folium_map)
    
    tilesets = {
#        these maps are no longer supported by Stamen
#        check back for 'Watercolor'        
#        "Terrain": 'Stamen Terrain',
        'Street Map': 'OpenStreetMap',
#        'Toner': 'Stamen Toner',
#        'Watercolor': 'Stamen Watercolor',
        'Positron': 'CartoDB positron',
        'Dark Matter': 'CartoDB dark_matter',
    }
    for name, tileset in tilesets.items():
        folium.TileLayer(tileset, name=name).add_to(folium_map)

def clean_coords(coord_series, force_neg=False):
    
    coord_series = coord_series.apply(
        pd.to_numeric, 
        errors='ignore', 
        downcast='float'
    )
    if not coord_series.apply(type).eq(str).any():
        if force_neg:
            return -1 * coord_series.abs()
        return coord_series
    results = []
    for idx, coord in coord_series.iteritems():
        if not str(coord).replace('.', '').replace('-', '').isnumeric():
            coord_strs = str(coord).split(' ')
            coord_digits = []
            for coord_str in coord_strs:
                coord_digit = ''.join([ch for ch in coord_str if ch.isdigit() or ch == '.'])
                coord_digits.append(float(coord_digit))
            dec = None
            coord_dec = 0
            for i in reversed(range(0, len(coord_digits))):
                if dec:
                    coord_dec = abs(coord_digits[i]) + dec
                dec = coord_digits[i] / 60
            if str(coord)[0] == '-':
                coord_dec = -1 * coord_dec
            results.append(coord_dec)
        else:
            results.append(coord)
    if force_neg:
        results[:] = [-1 * result if result > 0 else result for result  in results]
    clean_series = pd.Series(results, index=coord_series.index)
    return clean_series

def get_huc(geo_df, lat, lon, level='12'):

    for idx, row in geo_df.iterrows():
        polygon = row['geometry']
        point = Point(lon, lat)
        if polygon.contains(point):
            return row[f'HUC{level}']
    return None

def get_season():
    curr_month = datetime.now().month
    if curr_month > 3 and curr_month < 6:
        return 'spring'
    if curr_month > 5 and curr_month < 10:
        return 'summer'
    if curr_month > 9:
        return 'fall'
    return 'winter'

def add_huc_layer(level=2, gis_path='gis', embed=False, show=True, huc_filter=''):
    
    huc_str = f'HUC{level}'
    huc_geojson_path = path.join(gis_path, f'{huc_str}.geojson')
    with open(huc_geojson_path, 'r') as gj:
                huc_geojson = json.load(gj)
    try:
        weight = -0.25 * float(level) + 2.5
        if type(huc_filter) == int:
            huc_filter = str(huc_filter)
 
        if huc_filter:
            huc_style = lambda x: {
            'fillColor': '#ffffff00', 'color': '#1f1f1faa', 
            'weight': weight if x['properties'][huc_str].startswith(huc_filter) else 0
            }
            features = [
                i for i in huc_geojson['features'] if 
                i['properties'][huc_str].startswith(huc_filter)
            ]
            huc_geojson['features'] = features 
        else:
            huc_style = lambda x: {
                'fillColor': '#ffffff00', 'color': '#1f1f1faa', 'weight': weight
            }
        geojson = folium.GeoJson(
            huc_geojson,
            name=f'HUC {level}',
            style_function=huc_style,
            show=show,
            smooth_factor=1
        )
        return geojson
    except Exception as err:
        print(f'Could not add HUC {level} layer to map! - {err}')
        return None
    
def add_huc_chropleth(data_type='swe', show=False, huc_level='6', 
                      gis_path='gis', huc_filter='', use_topo=False):
    
    huc_str = f'HUC{huc_level}'
    stat_type_dict = {'swe': 'Median', 'prec': 'Median'}
    stat_type = stat_type_dict.get(data_type, '')
    layer_name = f'{huc_str} % {stat_type} {data_type.upper()}'
    if use_topo:
        topo_json_path = path.join(gis_path, f'{huc_str}.topojson')
        with open(topo_json_path, 'r') as tj:
            topo_json = json.load(tj)
        if huc_filter:
            topo_json = filter_topo_json(
                topo_json, huc_level=huc_level, filter_str=huc_filter
            )
    else:
        geo_json_path = path.join(gis_path, f'{huc_str}.geojson')
        with open(geo_json_path, 'r') as gj:
            geo_json = json.load(gj)
        if huc_filter:
            features = [
                i for i in geo_json['features'] if 
                i['properties'][huc_str].startswith(huc_filter)
            ]
            geo_json['features'] = features 
    style_function = lambda x: style_chropleth(
        x, data_type=data_type, huc_level=huc_level, huc_filter=huc_filter
    )
    tooltip = folium.features.GeoJsonTooltip(
        ['Name', f'{data_type}_percent', f'{data_type}_updt'],
        aliases=['Basin Name:', f'{layer_name}:', 'Updated:']
    )
    # tooltip = folium.features.GeoJsonTooltip(
    #     ['Name', f'{data_type}_percent', f'HUC{huc_level}'],
    #     aliases=['Basin Name:', f'{layer_name}:', 'ID:']
    # )
    try:
        if use_topo:
            topo_json = folium.TopoJson(
                topo_json,
                f'objects.{huc_str}',
                name=layer_name,
                overlay=True,
                show=show,
                smooth_factor=1,
                style_function=style_function,
                tooltip=tooltip
            )
            return topo_json
        else:
            geo_json = folium.GeoJson(
                geo_json,
                name=layer_name,
                embed=False,
                overlay=True,
                control=True,
                smooth_factor=3.0,
                style_function=style_function,
                show=show,
                tooltip=tooltip
            )
            return geo_json
    except Exception as err:
        print(f'Could not add HUC {data_type} chropleth layer to map! - {err}')
        return None

def style_chropleth(feature, data_type='swe', huc_level='2', huc_filter=''):
    colormap = get_colormap()
    if type(huc_filter) == int:
        huc_filter = str(huc_filter)
    huc_level = str(huc_level)
    stat_value = feature['properties'].get(f'{data_type}_percent', 'N/A')
    huc_id = str(feature['properties'].get(f'HUC{huc_level}', 'N/A'))
    if not stat_value == 'N/A':
        stat_value = float(stat_value)
    
    return {
        'fillOpacity': 
            0 if stat_value == 'N/A' or 
            not huc_id.startswith(huc_filter) else 
            0.75,
        'weight': 0,
        'fillColor': 
            '#00000000' if stat_value == 'N/A' or 
            not huc_id.startswith(huc_filter) else 
            colormap(stat_value)
    }


def get_colormap(low=50, high=150):
    
    colormap = branca.colormap.LinearColormap(
        colors=[
            (255,51,51,150), 
            (255,255,51,150), 
            (51,255,51,150), 
            (51,153,255,150), 
            (153,51,255,150)
        ], 
        index=[50, 75, 100, 125, 150], 
        vmin=50,
        vmax=150
    )
    colormap.caption = '% of Median Precipitation or % Median Snow Water Equivalent'
    return colormap

def filter_geo_json(geo_json_path, huc_level=2, filter_str=''):
   
    filter_attr = f'HUC{huc_level}'
    f_geo_json = {'type': 'FeatureCollection'}
    with open(geo_json_path, 'r') as gj:
        geo_json = json.load(gj)
    features = [i for i in geo_json['features'] if 
                i['properties'][filter_attr][:len(filter_str)] == filter_str]
    f_geo_json['features'] = features
    
    return f_geo_json

def filter_topo_json(topo_json, huc_level=2, filter_str=''):
    
    geometries = topo_json['objects'][f'HUC{huc_level}']['geometries']
    geometries[:] = [i for i in geometries if 
                i['properties'][f'HUC{huc_level}'][:len(filter_str)] == filter_str]
    topo_json['geometries'] = geometries
    return topo_json

if __name__ == '__main__':
    print('Just a utility module')
