# -*- coding: utf-8 -*-
"""

data_classification.py

Classify data values based on common classifiers

Created on Tue Nov 13 13:05:13 2018

@author: cscuser
"""

import geopandas as gpd
import pysal as ps

# Filepath
fp = "L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

# Read data
data = gpd.read_file(fp)

# exclude -1 values
data = data.loc[data['pt_r_tt']>=0]

# plot data based on fisher jenks with 9 classes and a matplotlib colormap
data.plot(column='pt_r_tt', scheme='Fisher_Jenks', k=9, cmap='RdYlBu', linewidth=0, legend=True)

#Define number of classes
k = 12

# Initialise the natural breaks classifier
classifier = ps.Natural_Breaks.make(k=k)

# Classify travel time values
classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt' (you can list multiple columns inside the curlies separated by commas)
classifications = classifications.rename(columns={'pt_r_tt': 'nb_pt_r_tt'})

# conduct table join based on index
data = data.join(classifications)

# Create a map based on new classes
ax = data.plot(column='nb_pt_r_tt', linewidth=0, legend=True)

# Create a custom classifier
class_bins = [10, 20, 30, 40, 50, 60]
classifier = ps.User_Defined.make(class_bins)

# Classify travel time values
custom_classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt' (you can list multiple columns inside the curlies separated by commas)
custom_classifications = custom_classifications.rename(columns={'pt_r_tt': 'c_pt_r_tt'})

# conduct table join based on index
data = data.join(custom_classifications)

# Create a map based on new classes
ax = data.plot(column='c_pt_r_tt', linewidth=0, legend=True)
