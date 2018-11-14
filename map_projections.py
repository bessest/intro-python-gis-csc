# -*- coding: utf-8 -*-
"""

map_projections.py

Introduction to Map projections

Created on Mon Nov 12 15:25:30 2018

@author: Bess Hardwick
"""

import geopandas as gpd
import matplotlib.pyplot as plt
# Read the file
fp = "L2_data/L2_data/Europe_borders.shp"
data = gpd.read_file(fp)

# Check the coordinate reference system
data.crs

# Let's make a copy of our data
geo = data.copy()

# Reproject the data
geo = geo.to_crs(epsg=3035)

# Check the new geometry values
print(data['geometry'].head())

# plot and see the difference
# ----------------------------------

# create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))

# plot wgs84 to ax1 and other to ax2
data.plot(ax=ax1, facecolor='gray')
geo.plot(ax=ax2, facecolor='blue')

# set titles
ax1.set_title("WGS84", fontsize=24)
ax2.set_title("ETRS Lambert Azimuthal Equal Area")

#save the figure on disk
plt.savefig("projections.png", dpi=300)

# save reprojected data to disk. In windows it might not save the prj!
outfp = "L2_data/L2_data/Europe_borders_epsg3035.shp"

# fix the crs
import pycrs
proj4 = pycrs.parser.from_epsg_code(3035).to_proj4()
geo.crs = proj4
geo.to_file(outfp)