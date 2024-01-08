# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:52 2024

@author: hendr
"""

import GIS_functions as gis
import os
import matplotlib.pyplot as plt
import numpy as np


locations = [location for location in os.listdir("OUT/Optical_images") if not location.startswith(".")]

for location in locations:
    for index_type in [index_type for index_type in os.listdir(f"OUT/Optical_images/{location}") if (not index_type == "JPEG_MAPS" and not index_type.startswith("."))]:
        # We initialize the index_arrays list, where the different arrays of pixel values of that
        # index type for that location (as calculated in Ex. 5) in the time series get stored.
        # The idea is then to take for each pixel (per location) the mean value of the index 
        # (NDVI or SAVI) throughout the whole time series
        index_arrays = []
        for index_map in gis.list_files_in_folder(f"OUT/Optical_images/{location}/{index_type}"):
            index_arrays.append(gis.open_as_array(index_map))

        # We calculate the array of pixel averages with np.nanmean. The function np.nanmean
        # has as effect that whenever a pixel has no index value at some point in time (and hence
        # has a NaN-value in its respective index array of that timepoint), that particular pixel
        # for that particular time is disregarded from the calculation of the average.
        index_average_array = np.nanmean(index_arrays, axis=0)

        # We store the so-calculated index average arrays as a tif-file with the same specs
        # as the land cover image of the corresponding location, to make sure we can make the
        # correct comparisons in Ex. 7.
        index_average_filename = f"OUT/Index_averages/{location}_{index_type}_average.tif"

        driver, ndv, xsize, ysize, geot, projection = gis.get_geoinfo(f"DATA/Land_Cover_images/LandCover_{location}.tif")
        
        gis.create_geotiff(index_average_filename,
                       array=index_average_array,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)
