# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:51 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt

from Ex2 import area_df

locations = area_df.index.droplevel(level="Land cover type").unique()

for location in locations:
    relative_area_land_cover_type = area_df[area_df.index.isin([location], level="Location")]["% of total area location"]
    land_cover_types = relative_area_land_cover_type.index.droplevel(level="Location").unique()
    plt.figure()
    plt.pie(relative_area_land_cover_type, labels=land_cover_types)
    plt.savefig(f"OUT/Pie_charts/{location}")