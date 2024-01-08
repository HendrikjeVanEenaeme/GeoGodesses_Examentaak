# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:28:33 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt

#We go over each land_cover_image in a loop and open them as arrays using GIS_functions
for land_cover_image in gis.list_files_in_folder("DATA/Land_Cover_images"):
    land_cover_data_array = gis.open_as_array(land_cover_image)
    
    #Now we define the path of where the output will be saved
    #We create a map called OUT in the cwd and within this map another map called Land_Cover_images
    out_fih = land_cover_image.replace("DATA", "OUT").replace(".tif", ".jpeg")

    #We create an empty figure and display on this figure the data as an image and save it
    plt.figure()
    plt.imshow(land_cover_data_array)
    plt.savefig(out_fih, dpi=600)
    
    