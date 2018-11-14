# -*- coding: utf-8 -*-
"""

mask_raster.py

How to use Rasterio to mask (clip) raster files

Created on Wed Nov 14 11:09:38 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs
import os
%matplotlib inline

# Data dir
data_dir = "L5_data"

# Input raster
fp = os.path.join(data_dir, "p188r018_7t20020529_z34__LV-FIN.tif")

# Output raster
out_tif = os.path.join(data_dir, "Helsinki_Masked.tif")

# Read the data
raster = rasterio.open(fp)

# Visualize the NIR band
show((raster, 4), cmap='terrain')

# WGS84 coordinates
minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

# create a geodataframe
crs_code = pycrs.parser.from_epsg_code(4326).to_proj4()
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=crs_code)
print(geo)

# Project the geodataframe into same CRS as the raster
geo = geo.to_crs(crs=raster.crs)

# Print crs
geo.crs


def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    features = [json.loads(gdf.to_json())['features'][0]['geometry']]
    return features

# convert geodataframe to geometric features dict
coords = getFeatures(geo)
print(coords)

# Clip the raster with Polygon
out_img, out_transform = mask(dataset=raster, shapes=coords, crop=True)

# Copy the metadata
out_meta = raster.meta.copy()
print(out_meta)

# Parse proj4 information to store with the raster
epsg_code = int(raster.crs.data['init'][5:])
print(epsg_code)
epsg_proj4 = pycrs.parser.from_epsg_code(epsg_code).to_proj4()

# update metadata with new dimensions, crs etc.
out_meta.update(
        {"height": out_img.shape[1],
         "width": out_img.shape[2],
         "transform": out_transform,
         "crs": epsg_proj4
         }
        )

# save the clipped raster to disk
with rasterio.open(out_tif, "w", **out_meta) as dest:
        dest.write(out_img)
        
# Open the clipped raster file
clipped = rasterio.open(out_tif)

# Visualize
show((clipped, 5), cmap='terrain')






