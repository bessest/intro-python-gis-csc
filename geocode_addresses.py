# -*- coding: utf-8 -*-
"""

geocode_addresses.py

How to convert addresses to points and vice versa


Created on Tue Nov 13 10:23:35 2018

@author: cscuser
"""

import geopandas as gpd
import pandas as pd
from geopandas.tools import geocode
import contextily as ctx

def add_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png', basemap=None, extent=None):

   """Adds basemap to figure"""    

   xmin, xmax, ymin, ymax = ax.axis()

   if basemap is None:

       basemap, extent = get_basemap(ax, zoom=zoom, url=url)

   ax.imshow(basemap, extent=extent, interpolation='bilinear')

   # restore original x/y limits

   ax.axis((xmin, xmax, ymin, ymax))

   return ax



def get_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png'):

   """Helper function to add a basemap for the plot"""

   xmin, xmax, ymin, ymax = ax.axis()

   basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=url)

   return basemap, extent

# filepath
fp = "L3_data/addresses.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

# geocode the addresses from 'addr'
geo = geocode(data['addr'], provider='nominatim', user_agent='csc_user_bh')

# merge geocoded locations back to the original dataframe
geo = geo.join(data)

#cut off, didn't finish
