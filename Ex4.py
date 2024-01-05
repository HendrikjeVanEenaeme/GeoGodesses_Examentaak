# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:00:51 2024

@author: hendr
"""

import GIS_functions as gis


# create a function to read the bands of a TIFF-file and calculate NDVI
def calc_NDVI(fih):
    RED_band = gis.open_as_array(fih, bandnumber=1)
    NIR_band = gis.open_as_array(fih, bandnumber=2)

    NDVI = (NIR_band - RED_band) / (NIR_band + RED_band)

    return NDVI


# create a function to read the bands of a TIFF-file and calculate SAVI
def calc_SAVI(fih):
    RED_band = gis.open_as_array(fih, bandnumber=1)
    NIR_band = gis.open_as_array(fih, bandnumber=2)

    SAVI = 1.5 * (NIR_band - RED_band) / (NIR_band + RED_band + 0.5)

    return SAVI