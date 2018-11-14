# -*- coding: utf-8 -*-
"""
geometric_objects.py

Intro to Shapely geometric objects and functionalities

Requirements:
    - shapely

Created on Mon Nov 12 10:59:31 2018

@author: Bess Hardwick
"""


# Import necessary geometric objects from shapely module
from shapely.geometry import Point, LineString, Polygon 

# Point
#-------------------

# Create Point geometric object(s) with coordinates
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

print(point3D)
type(point1)

#get the coordinates
point_coords = point1.coords

#get x and y coordinates
xy = point1.xy
print(xy)

#get x and y coordinates
x = point1.x
y = point1.y

#Calclate distance between point1 and point2
point_dist = point1.distance(point2)
print(point_dist)

#Create a buffer with distance of 20 units
point_buffer = point1.buffer(20)

# LineString
# ---------------------------

# create line based on Shapely points
line = LineString( [point1, point2, point3] )

# creat line based on coordinate tuples
line2 = LineString( [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

# get coordinates
lxy = line.xy

# get x and y coordinates
x = line.xy[0]
y = line.xy[1]

# get the length
l_length = line.length

#get the centroid
l_centroid = line.centroid

# Polygon
# ----------------------------

# create polygon based on coordinate tuples
poly = Polygon( [ (2.2, 4.2), (7.2, -25.1), (9.26, -2.456) ] )

# create polygon based on Points. This is list comprehension. 
# Putting commands in front of for is same as indentation. 

point_list = [point1, point2, point3]
poly2 = Polygon( [(p.x, p.y) for p in point_list ] )

# get geometry type as string
poly_type = poly.geom_type

# calculate area
poly_area = poly.area

#Centroid
poly_centroid = poly.centroid

#bounding box
poly_bbox = poly.bounds

# create bounding box geometry. Asterisk unpacks values from list
from shapely.geometry import box
bbox = box(*poly_bbox)

# Get exterior
poly_exterior = poly.exterior

# Length of exterior
poly_ext_length = poly.exterior.length

# Plygon with hole
# ------------------------

# First we define our exterior
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# Create a large hole leaving ten decimal degree boundary. Note multiple brackets
# for making multiple holes
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

world_polygon = Polygon(shell=world_exterior, holes = hole)
