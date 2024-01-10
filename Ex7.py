# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:01:58 2024

@author: hendr
"""

import GIS_functions as gis
import numpy as np
import os

from Ex2 import area_df

# We initiate the "Average NDVI" and "Average SAVI" in the dataframe from Ex2 with NaN values,
# soon to be replaced by the index averages per land cover type 
area_df[["Average NDVI", "Average SAVI"]] = np.nan

# We define a constant INDEX_TYPE, containing the different index types with which vegetation
# presence is measured. We loop over these variables later, to construct the correct paths
INDEX_TYPE = ["NDVI", "SAVI"]

# We loop over the different location and land cover types in the multi-index dataframe
for location, land_cover_type in area_df.index:
    # Per location we wish to calculate the various index averages (i.e.
    # NDVI and SAVI) for the different land cover types.
    for index_type in INDEX_TYPE:
        # index_average_array is the array containing the calculated index averages
        # per pixel
        index_average_array = gis.open_as_array(os.path.join('OUT', 'Index_averages', f'{location}_{index_type}_average.tif'))
        # land_cover array is the array containing the land cover type per pixel
        land_cover_array = gis.open_as_array(os.path.join('DATA', 'Land_Cover_images', f'LandCover_{location}.tif'))

        # For a given location and land cover type, we calculate the mean (disregarding NaN-values) 
        # of the index averages on pixels corresponding to that land cover type. We can filter on 
        # these pixels by using np.where, and the mean (without taking into account NaN-values) is
        # then calculated by np.nanmean. The resulting value is stored in the area_df column
        # that corresponds to that index, and with the multi-index of that row being the corresponding
        # location and land cover type
        area_df.loc[(location, land_cover_type), f"Average {index_type}"] = np.nanmean(index_average_array[np.where(land_cover_array==land_cover_type)])








