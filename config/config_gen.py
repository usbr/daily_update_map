# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:08:44 2020

@author: buriona
"""

'''
Keep in mind the top left corner of the button is the anchor point
positive offsets move buttons to the left and upwards
'''

forecasts = {}

config_name = 'test'
map_center = (41.4, -109.85)
initial_zoom = 9
huc_level = 4
huc_filter = [1404]
title = 'Test'
regions = {
    'Upper Green': {
        'coords': [41.6, -110.1], 'huc-level': 6, 'alias': None, 'anchor': (0,0)
    },

}

reservoirs = {
    'Flaming Gorge': {
        'coords': [40.91474, -109.42185], 'region': 'uc', 'anno': '', 'cap': 3671.0, 
        'id': 917, 'alias': None, 'anchor': (0,-15), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },

}
    
test_config = {
    config_name: {
        'huc_level': huc_level,
        'huc_filter': huc_filter,
        'zoom': initial_zoom, 
        'center': map_center, 
        'reservoirs': reservoirs, 
        'regions': regions, 
        'forecasts': forecasts
    }
}

ug_config_name = 'ug'
ug_map_center = (41.6, -109.7)
ug_initial_zoom = 9
ug_huc_level = 4
ug_huc_filter = [1404, 140500]
ug_title = 'Upper Green Basin'

ug_regions = {
    '140401_Upper_Green': {
        'coords': [41.6, -110.1], 'huc-level': 6, 'alias': 'Upper Green', 'anchor': (0,0)
    },
    '14040107_Blacks_Fork': {
        'coords': [41.3, -110.4], 'huc-level': 8, 'alias': 'Blacks Fork', 'anchor': (0,0)
    },
    '14040104_Big_Sandy': {
        'coords': [42.06, -109.64], 'huc-level': 8, 'alias': 'Big Sandy', 'anchor': (0,0)
    },
    '14040102_New_Fork': {
        'coords': [42.9, -109.8], 'huc-level': 8, 'alias': 'New Fork', 'anchor': (0,0)
    },
    '14040106_Upper_Green-Flaming_Gorge_Reservoir': {
        'coords': [41.12, -109.92], 'huc-level': 8, 'alias': 'Upper Green-Flaming Gorge', 'anchor': (0,0)
    },
    '14050003_Little_Snake': {
        'coords': [41.05, -108.08], 'huc-level': 8, 'alias': 'Little Snake', 'anchor': (0,0)
    },
    '14050001_Upper_Yampa': {
        'coords': [40.53, -107.35], 'huc-level': 8, 'alias': 'Upper Yampa', 'anchor': (0,0)
    },
    '14050005_Upper_White': {
        'coords': [40.02, -107.85], 'huc-level': 8, 'alias': 'Upper White', 'anchor': (0,0)
    },
    
}

ug_reservoirs = {
    'Flaming Gorge': {
        'coords': [40.91474, -109.42185], 'region': 'uc', 'anno': '', 'cap': 3671.0, 
        'id': 917, 'alias': None, 'anchor': (50,30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },
    'Fontenelle': {
        'coords': [42.02617, -110.06816], 'region': 'uc', 'anno': '', 'cap': 333.956, 
        'id': 916, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1717, 'elev': 1926, 'inflow': 1790, 'release': 1870}
    },
    'Eden': {
        'coords': [42.21665, -109.37087], 'region': 'uc', 'anno': '', 'cap': 13.164, 
        'id': 954, 'alias': None, 'anchor': (0,-20), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1752, 'elev': 1959, 'inflow': 1823, 'release': 1903}
    },
    'Big Sandy': {
        'coords': [42.24993, -109.42803], 'region': 'uc', 'anno': '', 'cap': 36.688, 
        'id': 936, 'alias': None, 'anchor': (0,20), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1734, 'elev': 1941, 'inflow': 1805, 'release': 1885}
    },
    'Meeks Cabin': {
        'coords': [41.01664, -110.58344], 'region': 'uc', 'anno': '', 'cap': 29.87, 
        'id': 944, 'alias': None, 'anchor': (25,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1742, 'elev': 1949, 'inflow': 1813, 'release': 1893}
    },
    'Stateline': {
        'coords': [40.98291, -110.39038], 'region': 'uc', 'anno': '', 'cap': 13.88, 
        'id': 949, 'alias': None, 'anchor': (-25,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1747, 'elev': 1954, 'inflow': 1818, 'release': 1898}
    }
}

ug_config = {
    ug_config_name: {
        'title': ug_title,
        'huc_level': ug_huc_level,
        'huc_filter': ug_huc_filter,
        'zoom': ug_initial_zoom, 
        'center': ug_map_center, 
        'reservoirs': ug_reservoirs, 
        'regions': ug_regions, 
        'forecasts': forecasts
    }
}     

pb_config_name = 'pb'
pb_map_center = (39.03, -111.05)
pb_initial_zoom = 9
pb_huc_level = 6
pb_huc_filter = [14060007, 14060009, 14070002, 14070003]
pb_title = 'Price/San Rafael Basins'

pb_regions = {
    '140600_Lower_Green': {
        'coords': [39.67, -111.53], 'huc-level': 6, 'alias': 'Lower Green', 'anchor': (0,0)
    },
    '140700_Upper_Colorado-Dirty_Devil': {
        'coords': [38.72, -111.86], 'huc-level': 6, 'alias': 'Dirty Devil', 'anchor': (0,0)
    },
    '14060007_Price': {
        'coords': [39.57, -110.85], 'huc-level': 8, 'alias': 'Price', 'anchor': (0,0)
    },
    '14060009_San_Rafael': {
        'coords': [39.06, -110.9], 'huc-level': 8, 'alias': 'San Rafael', 'anchor': (0,0)
    },
    '14070002_Muddy': {
        'coords': [38.75, -111.2], 'huc-level': 8, 'alias': 'Muddy', 'anchor': (0,0)
    },
    '14070003_Fremont': {
        'coords': [38.45, -111.76], 'huc-level': 8, 'alias': 'Fremont', 'anchor': (0,0)
    }
}

pb_reservoirs = {
    'Huntington North': {
        'coords': [39.38458, -111.09082], 'region': 'uc', 'anno': '', 'cap': 1105.91, 
        'id': 956, 'alias': None, 'anchor': (0,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1754, 'elev': 1961, 'inflow': 1825, 'release': 1905}
    },
    'Joes Valley': {
        'coords': [39.2901, -111.27888], 'region': 'uc', 'anno': '', 'cap': 61.59, 
        'id': 932, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1730, 'elev': 1937, 'inflow': 1801, 'release': 1881}
    },
    'Scofield': {
        'coords': [39.77656, -111.05074], 'region': 'uc', 'anno': '', 'cap': 65.8, 
        'id': 931, 'alias': None, 'anchor': (0,-10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1729, 'elev': 1936, 'inflow': 1800, 'release': 1880}
    }
}    

pb_config = {
    pb_config_name: {
        'title': pb_title,
        'huc_level': pb_huc_level,
        'huc_filter': pb_huc_filter,
        'zoom': pb_initial_zoom, 
        'center': pb_map_center, 
        'reservoirs': pb_reservoirs, 
        'regions': pb_regions, 
        'forecasts': forecasts
    }
} 
    
ub_config_name = 'ub'
ub_map_center = (40.2, -110.3)
ub_initial_zoom = 9
ub_huc_level = 6
ub_huc_filter = [14060003, 14060004, 14060005, 14060010]
ub_title = 'Uinta Basin'

ub_regions = {
    '140600_Lower_Green': {
        'coords': [40.4, -110.23], 'huc-level': 6, 'alias': 'Lower Green', 'anchor': (0,0)
    },
    '14060003_Duchesne': {
        'coords': [40.42, -110.65], 'huc-level': 8, 'alias': 'Duchesne', 'anchor': (0,0)
    },
    '14060010_Lower_Green-Diamond': {
        'coords': [40.35, -109.56], 'huc-level': 8, 'alias': 'Diamond', 'anchor': (0,0)
    },
    '14060004_Strawberry': {
        'coords': [40.2, -110.815], 'huc-level': 8, 'alias': 'Strawberry', 'anchor': (0,0)
    },
    '14060005_Lower_Green-Desolation_Canyon': {
        'coords': [39.86, -110.5], 'huc-level': 8, 'alias': 'Desolation Canyon', 'anchor': (0,0)
    },
}

ub_reservoirs = {
    'Soldier Creek': {
        'coords': [40.13564, -111.02659], 'region': 'uc', 'anno': '', 'cap': 1105.91, 
        'id': 962, 'alias': None, 'anchor': (55,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1760, 'elev': 1967, 'inflow': 1831, 'release': 1911}
    },
    'Starvation': {
        'coords': [40.19324, -110.44722], 'region': 'uc', 'anno': '', 'cap': 162.279, 
        'id': 928, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1726, 'elev': 1934, 'inflow': 1798, 'release': 1878}
    },
    'Steinaker': {
        'coords': [40.51456, -109.53275], 'region': 'uc', 'anno': '', 'cap': 36.148, 
        'id': 927, 'alias': None, 'anchor': (0,-14), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1725, 'elev': 1933, 'inflow': 1797, 'release': 1877}
    },
    'Red Fleet': {
        'coords': [40.57543, -109.42052], 'region': 'uc', 'anno': '', 'cap': 25.7, 
        'id': 960, 'alias': None, 'anchor': (0,12), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1758, 'elev': 1965, 'inflow': 1829, 'release': 1909}
    },
    'Moon Lake': {
        'coords': [40.57445, -110.50665], 'region': 'uc', 'anno': '', 'cap': 37.848, 
        'id': 930, 'alias': None, 'anchor': (-30,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1728, 'elev': 1935, 'inflow': 1799, 'release': 1879}
    },
    'Upper Stillwater': {
        'coords': [40.56565, -110.70044], 'region': 'uc', 'anno': '', 'cap': 31.382, 
        'id': 963, 'alias': None, 'anchor': (30,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1761, 'elev': 1968, 'inflow': 1832, 'release': 1912}
    },
    'Currant Creek': {
        'coords': [40.33841, -111.05821], 'region': 'uc', 'anno': '', 'cap': 15.464, 
        'id': 952, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1750, 'elev': 1957, 'inflow': 1821, 'release': 1901}
    }
}
  
ub_config = {
    ub_config_name: {
        'title': ub_title,
        'huc_level': ub_huc_level,
        'huc_filter': ub_huc_filter,
        'zoom': ub_initial_zoom, 
        'center': ub_map_center, 
        'reservoirs': ub_reservoirs, 
        'regions': ub_regions, 
        'forecasts': forecasts
    }
} 

gb_config_name = 'gb'
gb_map_center = (41.05, -111.6)
gb_initial_zoom = 9
gb_huc_level = 4
gb_huc_filter = [1601,160201,160202]
gb_title = 'Wasatch Front Basins'

gb_regions = {
    '1601_Bear': {
        'coords': [41.6, -112.75], 'huc-level': 4, 'alias': 'Bear', 'anchor': (0,0)
    },
    '160101_Upper_Bear': {
        'coords': [41.66, -111.21], 'huc-level': 6, 'alias': 'Upper Bear', 'anchor': (0,0)
    },
    '160102_Lower_Bear': {
        'coords': [41.6, -112.31], 'huc-level': 6, 'alias': 'Lower Bear', 'anchor': (0,0)
    },
    '16020203_Provo': {
        'coords': [40.54, -111.75], 'huc-level': 8, 'alias': 'Provo', 'anchor': (0,0)
    },
    '16020204_Jordan': {
        'coords': [40.7, -111.98], 'huc-level': 8, 'alias': 'Jordan', 'anchor': (0,0)
    },
    '16020202_Spanish_Fork': {
        'coords': [40.1, -111.58], 'huc-level': 8, 'alias': 'Spanish Fork', 'anchor': (0,0)
    },
    '160201_Weber': {
        'coords': [41.1, -111.85], 'huc-level': 6, 'alias': 'Weber', 'anchor': (0,0)
    },
    '1602_Great_Salt_Lake': {
        'coords': [40.77, -112.5], 'huc-level': 4, 'alias': 'Great Salt Lake', 'anchor': (0,0)
    },
    
}

gb_reservoirs = {
    'Willard Bay': {
        'coords': [41.37738, -112.08339], 'region': 'uc', 'anno': '', 'cap': 222.273, 
        'id': 925, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1723, 'elev': 1932, 'inflow': 1796, 'release': 1876}
    },
    'Jordanelle': {
        'coords': [40.59833, -111.42304], 'region': 'uc', 'anno': '', 'cap': 311.0, 
        'id': 964, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1762, 'elev': 1969, 'inflow': 1833, 'release': 1913}
    },
    'Deer Creek': {
        'coords': [40.40837, -111.52908], 'region': 'uc', 'anno': '', 'cap': 150.161, 
        'id': 953, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1751, 'elev': 1958, 'inflow': 1822, 'release': 1902}
    },
    'Causey': {
        'coords': [41.29828, -111.58591], 'region': 'uc', 'anno': '', 'cap': 7.07, 
        'id': 938, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1736, 'elev': 1943, 'inflow': 1807, 'release': 1887}
    },
    'Lost Creek': {
        'coords': [41.18318, -111.39905], 'region': 'uc', 'anno': '', 'cap': 22.501, 
        'id': 942, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1740, 'elev': 1947, 'inflow': 1811, 'release': 1891}
    },
    'Echo': {
        'coords': [40.96412, -111.43239], 'region': 'uc', 'anno': '', 'cap': 73.94, 
        'id': 941, 'alias': None, 'anchor': (-28,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1739, 'elev': 1946, 'inflow': 1810, 'release': 1890}
    },
    'East Canyon': {
        'coords': [40.92027, -111.60099], 'region': 'uc', 'anno': '', 'cap': 49.510, 
        'id': 940, 'alias': None, 'anchor': (28,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1738, 'elev': 1945, 'inflow': 1809, 'release': 1889}
    },
    'Rockport': {
        'coords': [40.78944, -111.40263], 'region': 'uc', 'anno': '', 'cap': 115.075, 
        'id': 947, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1745, 'elev': 1952, 'inflow': 1816, 'release': 1896}
    },
    'Hyrum': {
        'coords': [41.62117, -111.86099], 'region': 'uc', 'anno': '', 'cap': 14.734, 
        'id': 957, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1755, 'elev': 1962, 'inflow': 1826, 'release': 1906}
    },
    'Newton': {
        'coords': [41.8998, -111.97562], 'region': 'uc', 'anno': '', 'cap': 5.374, 
        'id': 959, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1757, 'elev': 1964, 'inflow': 1828, 'release': 1908}
    },      
    'Pineview': {
        'coords': [41.2684, -111.8009], 'region': 'uc', 'anno': '', 'cap': 222.273, 
        'id': 946, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': {'elev': 1951, 'inflow': 1815, 'release': 1895, 'storage': 1744}
    }
}    
 
gb_config = {
    gb_config_name: {
        'title': gb_title,
        'huc_level': gb_huc_level,
        'huc_filter': gb_huc_filter,
        'zoom': gb_initial_zoom, 
        'center': gb_map_center, 
        'reservoirs': gb_reservoirs, 
        'regions': gb_regions, 
        'forecasts': forecasts
    }
} 

sj_config_name = 'sj'
sj_map_center = (37, -108.0)
sj_initial_zoom = 9
sj_huc_level = 4
sj_huc_filter = 1408
sj_title = 'San Juan Basin'

sj_regions = {
    '1408_San_Juan': {
        'coords': [37, -108.26], 'huc-level': 4, 'alias': 'San Juan', 'anchor': (0,0)
    },
    '14080101_Upper_San_Juan': {
        'coords': [37, -107], 'huc-level': 8, 'alias': 'Upper San Juan', 'anchor': (0,0)
    },
    '14080102_Piedra': {
        'coords': [37.53, -107.34], 'huc-level': 8, 'alias': 'Piedra', 'anchor': (0,0)
    },
    # 'Blanco': {
    #     'coords': [38.7, -107.6], 'huc-level': 8, 'alias': 'Blanco', 'anchor': (0,0)
    # },
    '14080104_Animas': {
        'coords': [37.65, -107.8], 'huc-level': 8, 'alias': 'Animas', 'anchor': (0,0)
    },
    '14080105_Middle_San_Juan': {
        'coords': [36.9, -109], 'huc-level': 8, 'alias': 'Middle San Juan', 'anchor': (0,0)
    },
    '14080106_Chaco': {
        'coords': [36.45, -108.84], 'huc-level': 8, 'alias': 'Chaco', 'anchor': (0,0)
    },
    '14080107_Mancos': {
        'coords': [37.2, -108.7], 'huc-level': 8, 'alias': 'Mancos', 'anchor': (0,0)
    },
    '14080203_Montezuma': {
        'coords': [37.7, -109.28], 'huc-level': 8, 'alias': 'Montezuma', 'anchor': (0,0)
    },
    '14080204_Chinle': {
        'coords': [36.8, -109.8], 'huc-level': 8, 'alias': 'Chinle', 'anchor': (0,0)
    },
    
}

sj_reservoirs = {
    'Navajo': {
        'coords': [36.80063, -107.61203], 'region': 'uc', 'anno': '', 'cap': 1701.3, 
        'id': 920, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1720, 'elev': 1929, 'inflow': 1793, 'release': 1873}
    },
    'Vallecito': {
        'coords': [37.37834, -107.57486], 'region': 'uc', 'anno': '', 'cap': 125.442, 
        'id': 933, 'alias': None, 'anchor': (-85,-40), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1731, 'elev': 1938, 'inflow': 1802, 'release': 1882}
    },
    'Lemon': {
        'coords': [37.39538, -107.66269], 'region': 'uc', 'anno': '', 'cap': 39.792, 
        'id': 934, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1732, 'elev': 1939, 'inflow': 1803, 'release': 1883}
    },
    'McPhee': {
        'coords': [37.57588, -108.57307], 'region': 'uc', 'anno': '', 'cap': 381.0, 
        'id': 958, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1756, 'elev': 1963, 'inflow': 1827, 'release': 1907}
    },
    'Nighthorse': {
        'coords': [37.22392, -107.91694], 'region': 'uc', 'anno': '', 'cap': 115.075, 
        'id': 3083, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 14623, 'elev': 14621, 'inflow': 14617, 'release': 14620}
    },
    'Jackson': {
        'coords': [37.40186, -108.27342], 'region': 'uc', 'anno': '', 'cap': 9.951, 
        'id': 935, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1733, 'elev': 1940, 'inflow': 1804, 'release': 1884}
    },
}
 
sj_config = {
    sj_config_name: {
        'title': sj_title,
        'huc_level': sj_huc_level,
        'huc_filter': sj_huc_filter,
        'zoom': sj_initial_zoom, 
        'center': sj_map_center, 
        'reservoirs': sj_reservoirs, 
        'regions': sj_regions, 
        'forecasts': forecasts
    }
} 
    
gunn_config_name = 'gunn'
gunn_map_center = (38.5, -107.4)
gunn_initial_zoom = 9
gunn_huc_level = 6
gunn_huc_filter = 1402
gunn_title = 'Gunnison Basin'

gunn_reservoirs = {
    'Paonia': {
        'coords': [38.94919, -107.34347], 'region': 'uc', 'anno': '', 'cap': 15.522, 
        'id': 945, 'alias': None, 'anchor': (-10,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1743, 'elev': 1950, 'inflow': 1814, 'release': 1894}
    },
    'Ridgway': {
        'coords': [38.23636, -107.75914], 'region': 'uc', 'anno': '', 'cap': 82.98, 
        'id': 912, 'alias': None, 'anchor': (20,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1713, 'elev': 1922, 'inflow': 1786, 'release': 1860}
    },
    'Silver Jack': {
        'coords': [38.22692, -107.54041], 'region': 'uc', 'anno': '', 'cap': 13.0, 
        'id': 939, 'alias': None, 'anchor': (-20,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1737, 'elev': 1944, 'inflow': 1808, 'release': 1888}
    },
    'Taylor Park': {
        'coords': [38.81844, -106.60592], 'region': 'uc', 'anno': '', 'cap': 106.21, 
        'id': 948, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1746, 'elev': 1953, 'inflow': 1817, 'release': 1897}
    },
    'Blue Mesa': {
        'coords': [38.45305, -107.33677], 'region': 'uc', 'anno': '', 'cap': 827.95, 
        'id': 913, 'alias': None, 'anchor': (-40,35), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1714, 'elev': 1923, 'inflow': 1787, 'release': 1867}
    },
    'Morrow Point': {
        'coords': [38.45191, -107.53791], 'region': 'uc', 'anno': '', 'cap': 117.05, 
        'id': 914, 'alias': None, 'anchor': (10,-25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1715, 'elev': 1924, 'inflow': 1788, 'release': 1868}
    },
    'Crystal': {
        'coords': [38.51046, -107.62374], 'region': 'uc', 'anno': '', 'cap': 17.55, 
        'id': 915, 'alias': None, 'anchor': (-10,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1716, 'elev': 1925, 'inflow': 1789, 'release': 1869}
    },
}
    
gunn_regions = {
    '1402_Gunnison': {
        'coords': [38.7, -107.6], 'huc-level': 4, 'alias': 'Gunnison', 'anchor': (0,0)
    },
    '14020001_East-Taylor': {
        'coords': [39, -106.9], 'huc-level': 8, 'alias': 'East-Taylor', 'anchor': (0,0)
    },
    '14020003_Tomichi': {
        'coords': [38.5, -106.7], 'huc-level': 8, 'alias': 'Tomichi', 'anchor': (0,0)
    },
    '14020006_Uncompahgre': {
        'coords': [38.5, -108.1], 'huc-level': 8, 'alias': 'Uncompahgre', 'anchor': (0,0)
    },
    '14020005_Lower_Gunnison': {
        'coords': [38.7, -108.5], 'huc-level': 8, 'alias': 'Lower Gunnison', 'anchor': (0,0)
    },
    '13060001_Pecos_Headwaters': {
        'coords': [33, -105], 'huc-level': 8, 'alias': 'Pecos Headwaters', 'anchor': (0,0)
    },
    '14020004_North_Fork_Gunnison': {
        'coords': [39.04, -107.74], 'huc-level': 8, 'alias': 'North Fork Gunnison', 'anchor': (0,0)
    },
   
}

gunn_config = {
    gunn_config_name: {
        'title': gunn_title,
        'huc_level': gunn_huc_level,
        'huc_filter': gunn_huc_filter,
        'zoom': gunn_initial_zoom, 
        'center': gunn_map_center, 
        'reservoirs': gunn_reservoirs, 
        'regions': gunn_regions, 
        'forecasts': forecasts
    }
} 

rg_config_name = 'rg'
rg_map_center = (35, -106)
rg_initial_zoom = 7
rg_huc_level = 2
rg_huc_filter = [1301, 1302, 1303, 1305, 1306, 14080101]
rg_title = 'Rio Grande Basin'

rg_regions = {
    '13_Rio_Grande_Region': {
        'coords': [34.7, -106.5], 'huc-level': 2, 'alias': 'Rio Grande', 'anchor': (0,0)
    },
    '13060001_Pecos_Headwaters': {
        'coords': [35.6, -104.5], 'huc-level': 8, 'alias': 'Pecos Headwaters', 'anchor': (0,0)
    },
    '130100_Rio_Grande_Headwaters': {
        'coords': [37.9, -106.65], 'huc-level': 6, 'alias': 'Rio Grande Headwaters', 'anchor': (0,0)
    },
    '130202_Rio_Grande-Elephant_Butte': {
        'coords': [34.7, -108.2], 'huc-level': 6, 'alias': 'Middle Rio Grande', 'anchor': (0,0)
    },
    '130201_Upper_Rio_Grande': {
        'coords': [36.9, -106.85], 'huc-level': 6, 'alias': 'Upper Rio Grande', 'anchor': (0,0)
    },
    '14080101_Upper_San_Juan': {
        'coords': [37, -108.55], 'huc-level': 8, 'alias': 'Upper San Juan', 'anchor': (0,0)
    },
}

rg_reservoirs = {
    'Elephant Butte': {
        'coords': [33.15, -107.2], 'region': 'uc', 'anno': '', 'cap': 2010.900, 
        'id': 1119, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 2684, 'elev': 2685, 'inflow': 2686, 'release': 2688}
    },
    'Heron': {
        'coords': [36.6973, -106.6992], 'region': 'uc', 'anno': '', 'cap': 401.662, 
        'id': 2686, 'alias': None, 'anchor': (-60,-30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19176, 'elev': 19175, 'inflow': None, 'release': 19609}
    },
    'El Vado': {
        'coords': [36.5948, -106.7366], 'region': 'uc', 'anno': '', 'cap': 114.202, 
        'id': 2685, 'alias': None, 'anchor': (60,-30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19548, 'elev': 19547, 'inflow': None, 'release': 19626}
    },
    'Abiquiu': {
        'coords': [36.2686, -106.4551], 'region': 'uc', 'anno': '', 'cap': 186.820, 
        'id': 2729, 'alias': None, 'anchor': (0,-48), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19127, 'elev': 19126, 'inflow': None, 'release': 20055}
    },
    'Caballo': {
        'coords': [32.89646, -107.29219], 'region': 'uc', 'anno': '', 'cap': 224.464, 
        'id': 1094, 'alias': None, 'anchor': (0,-35), 'pop_dir': 'up',
        'sdis': 
            {'storage': 2678, 'elev': 2679, 'inflow': 2680, 'release': 2682}
    },
    'Sumner': {
        'coords': [34.62884, -104.3924], 'region': 'uc', 'anno': '', 'cap': 35.917, 
        'id': 943, 'alias': None, 'anchor': (0,-5), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1741, 'elev': 1948, 'inflow': 1812, 'release': 1892}
    },
    'Brantley': {
        'coords': [32.5442, -104.3814], 'region': 'uc', 'anno': '', 'cap': 42.602, 
        'id': 937, 'alias': None, 'anchor': (75,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1735, 'elev': 1942, 'inflow': 1812, 'release': 1892}
    },
    'Avalon': {
        'coords': [32.4908, -104.2522], 'region': 'uc', 'anno': '', 'cap': 4.466, 
        'id': 2684, 'alias': None, 'anchor': (-35,-10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19172, 'elev': 19171, 'inflow': None, 'release': 20821}
    },
    'Santa Rosa': {
        'coords': [35.0443, -104.6663], 'region': 'uc', 'anno': '', 'cap': 101.083, 
        'id': 2730, 'alias': None, 'anchor': (0,5), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19164, 'elev': 19165, 'inflow': 20826, 'release': 20578}
    },   
}

rg_config = {
    rg_config_name: {
        'title': rg_title,
        'huc_level': rg_huc_level,
        'huc_filter': rg_huc_filter,
        'zoom': rg_initial_zoom, 
        'center': rg_map_center, 
        'reservoirs': rg_reservoirs, 
        'regions': rg_regions, 
        'forecasts': forecasts
    }
}    

uc_config_name = 'uc'
uc_map_center = (39.6, -108.6)
uc_initial_zoom = 7
uc_huc_level = 2
uc_huc_filter = 14
uc_title = 'Upper Colorado Basin'

uc_regions = {
    '14_Upper_Colorado_Region': {
        'coords': [39.8, -110.7], 'huc-level': 2, 'alias': 'Upper Colorado', 'anchor': (0,0)
    },
    '140200_Gunnison': {
        'coords': [39.0, -108.3], 'huc-level': 6, 'alias': 'Gunnison', 'anchor': (0,0)
    },
    '140100_Colorado_Headwaters': {
        'coords': [40, -107.1], 'huc-level': 6, 'alias': 'Colorado Headwaters', 'anchor': (0,0)
    },
    '140500_White-Yampa': {
        'coords': [40.9, -107.9], 'huc-level': 6, 'alias': 'White-Yampa', 'anchor': (0,0)
    },
    '140401_Upper_Green': {
        'coords': [42.9, -110.5], 'huc-level': 6, 'alias': 'Upper Green', 'anchor': (0,0)
    },
    '140600_Lower_Green': {
        'coords': [40.5, -110.8], 'huc-level': 6, 'alias': 'Lower Green', 'anchor': (0,0)
    },
    '140700_Upper_Colorado-Dirty_Devil': {
        'coords': [38.2, -112.25], 'huc-level': 6, 'alias': 'Dirty Devil', 'anchor': (0,0)
    },
    '140300_Upper_Colorado-Dolores': {
        'coords': [37.7, -108.2], 'huc-level': 6, 'alias': 'Dolores', 'anchor': (0,0)
    },
    '140802_Lower_San_Juan': {
        'coords': [37.7, -110.2], 'huc-level': 6, 'alias': 'Lower San Juan', 'anchor': (0,0)
    },
    '140801_Upper_San_Juan': {
        'coords': [36.3, -108.5], 'huc-level': 6, 'alias': 'Upper San Juan', 'anchor': (0,0)
    },
}

uc_reservoirs = {
    'Fontenelle': {
        'coords': [42.026, -110.068], 'region': 'uc', 'anno': '', 'cap': 333.956, 
        'id': 916, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1717, 'elev': 1926, 'inflow': 1790, 'release': 1870}
    },
    'Flaming Gorge': {
        'coords': [41.0934, -109.5406], 'region': 'uc', 'anno': '', 'cap': 3671,
        'id': 917, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },
    'Blue Mesa': {
        'coords': [38.453, -107.337], 'region': 'uc', 'anno': '', 'cap': 827.95,
        'id': 913, 'alias': None, 'anchor': (-115,25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1714, 'elev': 1923, 'inflow': 1787, 'release': 1867}
    },
    'Morrow Point': {
        'coords': [38.452, -107.538], 'region': 'uc', 'anno': '', 'cap': 117.05,
        'id': 914, 'alias': None, 'anchor': (-15,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1715, 'elev': 1924, 'inflow': 1843, 'release': 1868}
    },
    'Crystal': {
        'coords': [38.51, -107.624], 'region': 'uc', 'anno': '', 'cap': 17.55,
        'id': 915, 'alias': None, 'anchor': (115,-25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1716, 'elev': 1925, 'inflow': 1844, 'release': 1869}
    },
    'Navajo': {
        'coords': [36.801, -107.612], 'region': 'uc', 'anno': '', 'cap': 1648,
        'id': 920, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1720, 'elev': 1929, 'inflow': 1793, 'release': 1873}
    },
    'Lake Powell': {
        'coords': [37.0688, -111.2439], 'region': 'uc', 'anno': '', 'cap': 23314,
        'id': 919, 'alias': None, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1719, 'elev': 1928, 'inflow': 1792, 'release': 1872}
    }
} 

uc_config = {
    uc_config_name: {
        'title': uc_title,
        'huc_level': uc_huc_level,
        'huc_filter': uc_huc_filter,
        'zoom': uc_initial_zoom, 
        'center': uc_map_center, 
        'reservoirs': uc_reservoirs, 
        'regions': uc_regions, 
        'forecasts': forecasts
    }
}

all_configs = {
    'uc': uc_config,
    'gunn': gunn_config,
    'gb': gb_config,
    'pb': pb_config,
    'rg': rg_config,
    'sj': sj_config,
    'ub': ub_config,
    'ug': ug_config
}

if __name__ == '__main__':

    import json
    import sys
    from os import path
    import argparse
    cli_desc = 'Creates Upper Colorado Daily Summary map configs for USBR.'
    parser = argparse.ArgumentParser(description=cli_desc)
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-A", "--add", help="adds current config to all_config.json", action="store_true")   
    parser.add_argument("-r", "--remove", help="removes a config from all_config.json", action="store_true")   
    args = parser.parse_args()
    
    if args.version:
        print('region_status.py v1.0')

    this_dir = path.dirname(path.realpath(__file__))
    
    if args.remove:
        print(f'Removing {args.remove} from all_config.json if present.')
        all_config_file_name = 'all_config.json'
        with open(all_config_file_name, 'r') as j:
            all_config = json.load(j)
        all_config.pop(args.remove, None)
        with open(all_config_file_name, 'w') as j:
            json.dump(all_config, j, indent=2, sort_keys=True)
        sys.exit(0)

    for config_name, config in all_configs.items():
        config_file_name = f'{config_name}_config.json'
        with open(config_file_name, 'w') as j:
            json.dump(config, j, indent=4, sort_keys=True)
        print(f'Created {config_file_name}.')
        if args.add:
            all_config_filename = 'all_config.json'
            all_config_path = path.join(this_dir, all_config_filename)
            with open(all_config_path, 'r') as j:
                all_config = json.load(j)
            all_config[config_name] = config[config_name]
            with open(all_config_path, 'w') as j:
                json.dump(all_config, j, indent=2, sort_keys=True)
            print(f'  added {config_file_name} to all_config.json.')
