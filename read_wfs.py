# -*- coding: utf-8 -*-
"""

read_wfs.py
Created on Tue Nov 13 09:13:09 2018

@author: cscuser
"""

# See all available drivers supported by GDAL

import geopandas as gpd
import requests
import geojson
import pycrs

# Specify the url for the backend
url = 'http://geo.stat.fi/geoserver/vaestoruutu/wfs'

# get capabilities
capabilities_params = dict(service='WFS', request = 'GetCapabilities')

#Request
capabilities = requests.get(url, params=capabilities_params)
print(capabilities.content)

#Specify the parameters for fetching the data
params = dict(service='WFS', version='2.0.0', request='GetFeature',
         typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

# Fetch data from WFS using requests
r = requests.get(url, params=params)

# Create GeoDataFrame from geojson
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

# define crs
# data.crs = {'init': 'epsg:3067'}  # this might not work in windows
data.crs = pycrs.parser.from_epsg_code(3067).to_proj4()

# set geometry
data = data.set_geometry('geometry')

# remove column with lists
data = data.drop('bbox', axis=1)

# save to disk
outfp = "L2_data/L2_data/Population_grid_5km.shp"
data.to_file(outfp)
