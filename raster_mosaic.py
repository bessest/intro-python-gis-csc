# -*- coding: utf-8 -*-
"""

raster_mosaic.py

How to create a raster mosaic using rasterio

Created on Wed Nov 14 13:21:56 2018

@author: Bess Hardwick
"""

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
import pycrs
%matplotlib inline

# File and folder paths
data_dir = "L5_data"
out_fp = os.path.join(data_dir, "Helsinki_DEM_2x2m_mosaic.tif")

# Make a search criteria to select the DEM files
search_criteria = "L*.tif"
q = os.path.join(data_dir, search_criteria)
print(q)

# list files that match the criteria
dem_fps = glob.glob(q)
dem_fps

# open the source files with rasterio, using list comprehension!
src_files_to_mosaic = [ rasterio.open(fp) for fp in dem_fps ]

# other way from course materials:
## glob function can be used to list files from a directory with specific criteria
# dem_fps = glob.glob(q)

## Files that were found:
# dem_fps

# merge the rasters into a mosaic
mosaic, out_trans = merge(datasets=src_files_to_mosaic)

# plot
show(mosaic, cmap='terrain')

# update metadata and save the mosaic
out_meta = src_files_to_mosaic[0].meta.copy()

# update metadata with new dimensions and crs
out_meta.update(
        {'height': mosaic.shape[1],
         'width': mosaic.shape[2],
         'transform': out_trans,
         'crs': "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs " 
         }
        )

# write the mosaic to disk
with rasterio.open(out_fp, 'w', **out_meta) as dest:
    dest.write(mosaic)
    
# plot
m = rasterio.open(out_fp)
%matplotlib inline
plt.imshow(m.read(1), cmap = 'terrain')
plt.colorbar()

