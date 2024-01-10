# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:52 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt
import numpy as np
import os


for location in ["35MPT", "35MQS"]:
    for index_type in ["NDVI", "SAVI"]:
        # We initialize the index_arrays list, where the different arrays of pixel values of that
        # index type for that location (as calculated in Ex. 5) in the time series get stored.
        index_arrays = []
        for index_image in gis.list_files_in_folder(os.path.join("OUT", "Optical_images", location, index_type)):
            index_arrays.append(gis.open_as_array(index_image))
            
        # We calculate the array of pixel averages with np.nanmean 
        # This function disregards pixels with no index value (NaN-values) from the calculation
        index_average_array = np.nanmean(index_arrays, axis=0)

        # We store the index average arrays as a tif-file with the same specs
        # as the land cover image of the corresponding location, to make sure we can make the
        # correct comparisons in Ex. 7.
        index_average_filename = f'{os.path.join("OUT", "Index_averages", f"{location}_{index_type}_average")}.tif'

        driver, ndv, xsize, ysize, geot, projection = gis.get_geoinfo(os.path.join('DATA', 'Land_Cover_images', f'LandCover_{location}.tif'))
        
        gis.create_geotiff(index_average_filename,
                       array=index_average_array,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)
        
        
        #We create an average NDVI and average SAVI map per location 
        mapname = os.path.basename(index_average_filename).removesuffix(".tif")
        
        plt.figure()
        plt.imshow(index_average_array, cmap='YlGn', vmin=0, vmax=1)
        plt.title(f" Average Map - {mapname}")
        plt.colorbar(label="Value")
        plt.savefig(f'{os.path.join("OUT", "Index_averages", "JPEG_MAPS_averages", mapname)}.jpeg', dpi = 600)
        plt.close()

 
