# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:52 2024

@author: hendr
"""

import GIS_functions as gis
import matplotlib.pyplot as plt
import numpy as np
import os

from Ex4 import calc_NDVI, calc_SAVI



#create a loop for all files in optical images folder
#create variables filename and location to structure the output
for optical_image in gis.list_files_in_folder(os.path.join("DATA","Optical_images")): 
    filename = os.path.basename(optical_image)
    print(fil)
    location = filename.removesuffix(".tif").split('_')[-1].removeprefix("T")

#calling metadata of the source files
    driver, ndv, xsize, ysize, geot, projection = gis.get_geoinfo(optical_image)
    
#calling the functions of ex4
    NDVI = calc_NDVI(optical_image) 
    SAVI = calc_SAVI(optical_image)

#export the output as TIF-files
    gis.create_geotiff(os.path.join("OUT", "Optical_images", location, "NDVI", filename),
                       array=NDVI,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)

    gis.create_geotiff(os.path.join("OUT", "Optical_images", location, "SAVI", filename),
                       array=SAVI,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)
    
#create a NDVI and SAVI map per optical image 
    mapname = filename.removesuffix(".tif")

    plt.figure()
    plt.imshow(NDVI, cmap='YlGn', vmin=0, vmax=1)
    plt.title(f"NDVI Map - {mapname}")
    plt.colorbar(label="NDVI Value")
    plt.savefig(f'{os.path.join("OUT", "Optical_images", location, "JPEG_MAPS", "NDVI", mapname)}.jpeg', dpi = 600)
    plt.close()

    plt.figure()
    plt.imshow(SAVI, cmap='YlGn', vmin=0, vmax=1)
    plt.title(f"SAVI Map - {mapname}")
    plt.colorbar(label="SAVI Value")
    plt.savefig(f'{os.path.join("OUT", "Optical_images", location, "JPEG_MAPS", "SAVI", mapname)}.jpeg', dpi = 600)
    plt.close()


    
    
  
