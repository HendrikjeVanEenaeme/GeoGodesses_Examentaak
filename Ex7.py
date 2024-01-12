# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:01:58 2024

@author: hendr
"""

import GIS_functions as gis
import numpy as np
import os

from Ex2 import area_df

# We add the new columns "Average NDVI" and "Average SAVI" in the multi-index dataframe 
area_df[["Average NDVI", "Average SAVI"]] = np.nan

#We define a variable INDEX_TYPES, with the two different index types
INDEX_TYPES = ["NDVI", "SAVI"]

# We loop over the different location and land cover types in the multi-index dataframe
for location, land_cover_type in area_df.index:
    # Per location and land cover type, we wish to calculate the various index averages
    for index_type in INDEX_TYPES:
        # index_average_array is the array containing the calculated index averages per pixel
        index_average_array = gis.open_as_array(os.path.join('OUT', 'Index_averages', f'{location}_{index_type}_average.tif'))
        # land_cover array is the array containing the land cover type per pixel
        land_cover_array = gis.open_as_array(os.path.join('DATA', 'Land_Cover_images', f'LandCover_{location}.tif'))

        # We calculate the mean of the index average on pixels corresponding to 
        # the land cover type we are looping over.
        # The results are stored in the right place in our multi-index dataframe
        area_df.loc[(location, land_cover_type), f"Average {index_type}"] = np.nanmean(index_average_array[np.where(land_cover_array==land_cover_type)])





