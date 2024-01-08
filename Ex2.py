# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:49 2024

@author: hendr
"""

import GIS_functions as gis
import numpy as np
import os
import pandas as pd

#Create an empty Pandas dataframe to store information in python
area_df = pd.DataFrame()

#To loop through each file in the DATA/Land_Cover_images folder, get geospatial info on the current land cover image and extract location information from the filename by splitting it up
for land_cover_image in gis.list_files_in_folder(os.path.join("Data", "Land_Cover_images")):
    geo_info = gis.get_geoinfo(land_cover_image)
    location = land_cover_image.split('/')[-1].removesuffix('.tif').split('_')[-1]
    
    #calculate the total number of pixels
    total_number_pixels = geo_info[2] * geo_info[3]
    
    pixel_values = gis.open_as_array(land_cover_image)

    #To count pixel values (=land cover type) and how often they occure 
    land_cover_types, pixel_counts = np.unique(pixel_values, return_counts=True)
    #To calculate the absolute and relative area of each land cover type in square kilometres ans as a percentage of the total area
    absolute_area_land_cover_type = pixel_counts / 10000
    relative_area_land_cover_type = (pixel_counts / total_number_pixels) *100
    
    #Creating Pandas Dataframe to store the results for the current image 
    df = pd.DataFrame({"Location": location,
                       "Land cover type": land_cover_types,
                       "Area [km^2]": absolute_area_land_cover_type,
                       "% of total area location": relative_area_land_cover_type})
    #Adding new dataframe to already existing dataframe
    area_df = pd.concat([area_df, df])

#Setting a multi-level index using the columns 'Location' and 'Land cover type'
area_df = area_df.set_index(keys=["Location", "Land cover type"])