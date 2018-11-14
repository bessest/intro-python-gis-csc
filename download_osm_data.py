# -*- coding: utf-8 -*-
"""
download_osm_data.py

Use OSMnx package to download OSM data using OpverPass API

Created on Tue Nov 13 11:18:11 2018

@author: cscuser
"""

import osmnx as ox
import matplotlib.pyplot as plt

# Specify the name of the area of intersrt for us
place_name = "Kamppi, Helsinki, Finland"

# Retrieve the data from OSM
graph = ox.graph_from_address(place_name)

# Plot the streets
fig, ax = ox.plot_graph(graph)

# convert the graph to GeoDataFrames
node, edges = ox.graph_to_gdfs(graph)

# retrieve buildings from OSM
buildings = ox.buildings_from_address(place_name, distance = 1000)

# plot the buildings
buildings.plot()

# footprint of kamppi
footprint = ox.gdf_from_place(place_name)
footprint.plot()

# retrieve points of interest from OSM
restaurants = ox.pois_from_place(place_name, amenities=['restaurant', 'bar'])
restaurants.plot()

# Plot all layers together
ax = footprint.plot(facecolor='black')
ax = edges.plot(ax=ax, linewidth=1, edgecolor = '#BC8F8F')
ax = buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
ax = restaurants.plot(ax=ax, color='green', alpha=0.7, markersize=10)