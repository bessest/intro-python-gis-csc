# -*- coding: utf-8 -*-
"""
spatial_join.py

How to coduct spatial join using geopandas

Created on Tue Nov 13 14:47:19 2018

@author: cscuser
"""

import geopandas as gpd

# filepath

pop_fp = "L4_data/Vaestotietoruudukko_2015.shp"
point_fp = "L4_data/addresses.shp"

# read the data
pop = gpd.read_file(pop_fp)
point= gpd.read_file(point_fp)

# Ensure that the datasets are in the same projection
point = point.to_crs(crs=pop.crs)

# cheeck that crs matches, get error message if not
assert pop.crs == point.crs, "The CRS of the layers do not match!"

# make spatial join
join = gpd.sjoin(point, pop, how='inner', op='within')

#visualise
join.plot(column='ASUKKAITA', cmap='Reds', markersize=join['ASUKKAITA']/1642*100, legend=True)
