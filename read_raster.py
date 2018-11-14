# -*- coding: utf-8 -*-
"""

read_raster.py


Created on Wed Nov 14 12:54:20 2018

@author: cscuser
"""

import rasterio
import os
import numpy as np
%matplotlib inline

# Data dir
data_dir = "L5_data"
fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# Open the file:
raster = rasterio.open(fp)

# Check type of the variable 'raster'
type(raster)

# Projection
raster.crs

# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform

# Dimensions
print(raster.width)
print(raster.height)

# Number of bands
raster.count

# Bounds of the file
raster.bounds

# Driver (data format)
raster.driver

# No data values for all channels
raster.nodatavals

# All Metadata for the whole raster dataset
raster.meta

# Read the raster band as separate variable
band1 = raster.read(1)

# Check type of the variable 'band'
print(type(band1))

# Data type of the values
print(band1.dtype)

# Read all bands
array = raster.read()

# Calculate statistics for each band
stats = []
for band in array:
    stats.append({
        'min': band.min(),
        'mean': band.mean(),
        'median': np.median(band),
        'max': band.max()})

# Show stats for each channel
stats
