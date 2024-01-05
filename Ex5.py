# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:52 2024

@author: hendr
"""

import GIS_functions as gis


from Ex4 import calc_NDVI, calc_SAVI


for optical_image in gis.list_files_in_folder("DATA\\Optical_images"): #insert file path to optical images folder
    filename = optical_image.split('\\')[-1]
    location = filename.removesuffix(".tif").split('_')[-1].removeprefix("T")

    driver, ndv, xsize, ysize, geot, projection = gis.get_geoinfo(optical_image)

#calling the functions of ex4
    NDVI = calc_NDVI(optical_image) 
    SAVI = calc_SAVI(optical_image)


    gis.create_geotiff(f"OUT\\Optical_images\\{location}\\NDVI\\{filename}",
                       array=NDVI,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)

    gis.create_geotiff(f"OUT\\Optical_images\\{location}\\SAVI\\{filename}",
                       array=SAVI,
                       driver=driver,
                       ndv=ndv,
                       xsize=xsize,
                       ysize=ysize,
                       geot=geot,
                       projection=projection)
    

    
    
  
