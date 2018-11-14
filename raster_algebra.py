# -*- coding: utf-8 -*-
"""

raster_algebra.py

Created on Wed Nov 14 12:59:39 2018

@author: cscuser
"""

import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt
%matplotlib inline

# Data dir
data_dir = "L5_data"

# Filepath
fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# Open the raster file in read mode
raster = rasterio.open(fp)

# Read red channel (channel number 3)
red = raster.read(3)
# Read NIR channel (channel number 4)
nir = raster.read(4)


# Calculate some stats to check the data
print(red.mean())
print(nir.mean())
print(type(nir))

# Visualize
show(nir, cmap='terrain')

# convert to floats
red = red.astype('f4')
nir = nir.astype('f4')

# ignore division by zero exceptions
np.seterr(divide='ignore', invalid='ignore')

# calculate NDVI
ndvi = (nir - red) / (nir + red)

# Plot the NDVI with legend
plt.imshow(ndvi, cmap='terrain_r')
plt.colorbar()

# time series
# change = year2018 - year2008