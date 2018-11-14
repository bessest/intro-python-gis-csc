# -*- coding: utf-8 -*-
"""

read_cloud_optimised_geotiffs.py

Created on Wed Nov 14 15:04:45 2018

@author: Bess Hardwick
"""

import rasterio
import matplotlib.pyplot as plt
import numpy as np
from rasterio.plot import show

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

# get the profile
src = rasterio.open(url)

#with rasterio.open(url) as src:
#    print(src.profile)
    
# get the list of overviews for band 1 and get the smallest one with the highest factor
oviews = src.overviews(1)
oview = oviews[-1]   

# read a thumbnail using low resolution source
thumbnail = src.read(1, out_shape =(1, int(src.height // oview), int(src.width // oview)) )

# plot
show(thumbnail, cmap='terrain')

# retrieve a "window" subset from full resolution raster
window = rasterio.windows.Window(1024, 1024, 1280, 2560)

# retrieve a subset of the data
subset = src.read(1, window=window)

# plot the subset
show(subset, cmap='terrain')

