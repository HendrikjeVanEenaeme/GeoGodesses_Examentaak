# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:51 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt 
import os

from Ex2 import area_df

locations = area_df.index.droplevel(level="Land cover type").unique()

for location in locations:
    relative_area_land_cover_type = area_df[area_df.index.isin([location], level="Location")]["% of total area location"]
    land_cover_types = relative_area_land_cover_type.index.droplevel(level="Location").unique()

#Create a pie chart with title and legend that shows the relative area of land cover type and save as jpeg
    plt.figure(figsize=(8, 8)) 
    plt.pie(relative_area_land_cover_type)
    plt.title(f"Land Cover Distribution in {location}")
    plt.legend(land_cover_types, title="Land Cover Types", bbox_to_anchor=(0.87, 1), loc="upper left")
    plt.savefig(f"{os.path.join('OUT', 'Pie_charts', location)}.jpeg", dpi = 600) #To save the figure as a jpeg
    