# -*- coding: utf-8 -*-
"""
geopandas_intro.py

Basic functionalities of geopandas library

Created on Mon Nov 12 13:17:25 2018

@author: Bess Hardwick
"""

# Import geopandas, and pandas if u like
import geopandas as gpd
import pandas as pd

# Filepath
fp = "L2_data/L2_data/DAMSELFISH_distributions.shp"

#read the file with geopandas
data = gpd.read_file(fp)

# print the first rows of the data

data.head(5)

# print columns
cols = data.columns

# plot the geometries. 
data.plot()

# write the first 50 rows of our data into a new shapefile
outfp = "L2_data/L2_data/DAMSELFISH_selection.shp"
outfp2 = "L2_data/L2_data/DAMSELFISH_selection.geojson"

# select the first rows
selection = data.head(50)

# save the selection
selection.to_file(outfp)

# save as geojson
selection.to_file(outfp2, driver = 'GeoJSON')

# Geometries in GeoDataFrame
# ------------------------------

# look: the last column is geometry
data.columns
data[['geometry', 'BINOMIAL']].head()

#select rows based on criteria

# Unique species
unique = data['BINOMIAL'].unique()
criteria = 'Stegastes redemptus'

# select rows
fish_a = data.loc[data['BINOMIAL']==criteria]
# fish_a = data.loc[(data['ValueX']>10) & (data['ValueY']<100)]

#postgis
#import psycopg2
#initialize connection with driver such as psycopg2
#conn, cursor = psycopg2.connect()
#pgdata = gpd.read_postgis(sql="SELECT * FROM TABLEX FETCH FIRST 10 ROWS;", con=conn)

# iterating rows in geopandas / pandas
# ---------------------------------------------------------
# Alternative 1: Iterate over GeoDataFrame. This is slow
for index, row in selection.iterrows():
    #calculate the area of each polygon
    poly_area = row['geometry'].area
    print(poly_area)
    
# this is faster
    
#alternative2
data['area'] = data.apply(lambda row: row['geometry'].area, axis = 1)

#alternative3
def calculate_area(row):
    return row['geometry'].area

data['area2'] = data.apply(calculate_area, axis = 1)

#geometric attributes from geodataframe
#-------------------------------------
# calculate the area using geopandas directly
data['area3'] = data.area
data['centroid'] = data.centroid

#geodataframes can have multiple geometry columns but this will cause trouble when saving as shapefile, pick a column

# set the geometry source for geodataframe
geo = data.copy()
geo = geo.set_geometry('centroid')   
geo.plot()

# create a buffer from points
#geo['buffer'] = geo.buffer(10)
#geo = geo.set_geometry('buffer')
#geo.plot()

# drop the 'geometry' column from gdf
geo = geo.drop('geometry', axis=1)

# save points
geo.to_file('geom_centroids.shp')

# calculate basic statistics. std, median etc
mean_area = geo['area'].mean()
min_area = geo['area'].min()

#calculate in (Geo)DataFrame
geo['areaX2'] = geo['area'] + geo['area2']
