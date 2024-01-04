# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:49 2024

@author: hendr
"""

import GIS_functions as gis
import numpy as np
import pandas as pd

area_df = pd.DataFrame()

for land_cover_image in gis.list_files_in_folder("DATA/Land_Cover_images"):
    geo_info = gis.get_geoinfo(land_cover_image)
    location = land_cover_image.split('/')[-1].removesuffix('.tif').split('_')[-1]

    total_number_pixels = geo_info[2] * geo_info[3]
    pixel_values = gis.open_as_array(land_cover_image)

    land_cover_types, pixel_counts = np.unique(pixel_values, return_counts=True)

    absolute_area_land_cover_type = pixel_counts * 100
    relative_area_land_cover_type = pixel_counts / total_number_pixels
    
    df = pd.DataFrame({"Location": location,
                       "Land cover type": land_cover_types,
                       "Area [m^2]": absolute_area_land_cover_type,
                       "% of total area location": relative_area_land_cover_type})

    area_df = pd.concat([area_df, df])
    
area_df = area_df.set_index(keys=["Location", "Land cover type"])

