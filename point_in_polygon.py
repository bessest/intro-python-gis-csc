# -*- coding: utf-8 -*-
"""
point_in_polygon.py

How to conduct Point in Polygon queries in Geopandas

Created on Tue Nov 13 13:50:58 2018

@author: cscuser
"""

import geopandas as gdp
import matplotlib.pyplot as plt
import shapely.speedups
gdp.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
shapely.speedups.enable()

#FIlepath
fp = "L4_data/PKS_suuralue.kml"
fpa = "L4_data/addresses.shp"

# read file
polys = gdp.read_file(fp, driver='KML')
data = gdp.read_file(fpa)

# select the area of interest
southern = polys.loc[polys['Name'] == 'Eteläinen']

# reset index and drop original index column
southern = southern.reset_index(drop=True)

# conduct Point in Polygon query
pip_mask = data.within(southern.loc[0, 'geometry'])

# select the pointes that were within the polygon

pip_data = data.loc[pip_mask]

# visualise the selection
ax = polys.plot(facecolor='gray')
ax = southern.plot(ax=ax, facecolor='red')
ax = pip_data.plot(ax=ax, color='gold', markersize=3)

