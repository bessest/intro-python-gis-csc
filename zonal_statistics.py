# -*- coding: utf-8 -*-
"""
zonal_statistics.py

How to calculate zonal stats using rasterio and rasterstats

Created on Wed Nov 14 13:53:18 2018

@author: Bess Hardwick
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
import os
import matplotlib.pyplot as plt

# filepath
data_dir = "L5_data"
dem_fp = os.path.join(data_dir, "Helsinki_DEM_2x2m_mosaic.tif")

# read the data
dem = rasterio.open(dem_fp)

# fetch the polygons for zonal stats from OSM
kallio_q = "Kallio, Helsinki, Finland"
pihlajamaki_q = "Pihlajamäki, Malmi, Helsinki, Finland"

# retrieve the geometries from OSM
kallio = ox.gdf_from_place(kallio_q)
pihlajamaki = ox.gdf_from_place(pihlajamaki_q)

# test that crs matches
assert kallio.crs == dem.crs, "CRS does not match between layers"
assert pihlajamaki.crs == dem.crs, "CRS does not match between layers"

# repriject the polygon to same projection as raster
kallio = kallio.to_crs(crs=dem.crs)
pihlajamaki = pihlajamaki.to_crs(crs=dem.crs)

# plot the areas on top of the raster
ax = kallio.plot(facecolor='None', edgecolor='red', linewidth=2)
ax = pihlajamaki.plot(ax=ax, facecolor='None', edgecolor='blue', linewidth=2)

# plot the raster below
show((dem, 1), ax=ax)

# use zonal statistics to assess which area is higher in elevation
# ---------------------------------------------------------------

# read the data
array = dem.read(1)

# get the affine
affine = dem.transform

# calculate zonal statistics
zs_kallio = zonal_stats(kallio, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
zs_pihlajamaki = zonal_stats(pihlajamaki, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])

# extra! which one is higher. access the list and a value in the list
if zs_kallio[0]['max'] > zs_pihlajamaki[0]['max']:
    print("Kallio is higher!")
else: 
    print("Pihlajamaki is higher!")

#extra extra! iterate over four channels
zs_results = {}

for channel in range(1,5):
    zs_results[channel] = zonal_stats(polygon, channel_data_array, stats=['min', 'max'])
