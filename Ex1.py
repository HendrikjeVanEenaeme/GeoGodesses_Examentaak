# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:28:33 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt

for land_cover_image in gis.list_files_in_folder("DATA/Land_Cover_images"):
    land_cover_data_array = gis.open_as_array(land_cover_image)

    out_fih = land_cover_image.replace("DATA", "OUT").replace(".tif", ".jpeg")

    plt.figure()
    plt.imshow(land_cover_data_array)
    plt.savefig(out_fih, dpi=600)
    
    