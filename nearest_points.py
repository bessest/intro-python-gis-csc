# -*- coding: utf-8 -*-
"""
nearest_points.py

How to get the nearest point of another one

Created on Tue Nov 13 15:12:20 2018

@author: cscuser
"""

from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd

def nearest(row, geom_union, df1, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """
    Finds the closest point from a set of points.
    
    Parameters
    ---------
    geom_union : shapely.MultiPoint
    """
    
    # find the geometry that is closesst
    nearest = df2['geometry'] == nearest_points(row['geometry'], geom_union)[1]
    
    #get the corresponding values from df2
    value = df2[nearest][src_column].get_values()[0]
    return value

#filepaths
fp1 = "L4_data/PKS_suuralue.kml"
fp2 = "L4_data/addresses.shp"

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# read data
polys = gpd.read_file(fp1)
src_points = gpd.read_file(fp2)

# unary union
unary_union = src_points.unary_union

# calculate the centroid for the polygons
polys['centroid'] = polys.centroid


# find the nearest public transport station for each polygon centroid.
polys['nearest_id'] = polys.apply(nearest, geom_union=unary_union, df1=polys, df2=src_points, geom1_col='centroid', src_column='id', axis=1)

