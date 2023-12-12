#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:42:15 2023

@author: lenie
"""

import os
import datetime
import calendar
import collections
import subprocess
import csv
from osgeo import gdal, osr
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy as np

gdal.UseExceptions()

def get_geoinfo(fih, subdataset=0):
    """
    Substract metadata from a geotiff, HDF4 or netCDF file.

    Parameters
    ----------
    fih : str
        Filehandle to file to be scrutinized.
    subdataset : int, optional
        Layer to be used in case of HDF4 or netCDF format, default is 0.

    Returns
    -------
    driver : str
        Driver of the fih.
    ndv : float
        No-data-value of the fih.
    xsize : int
        Amount of pixels in x direction.
    ysize : int
        Amount of pixels in y direction.
    geot : list
        List with geotransform values.
    Projection : str
        Projection of fih.
    """
    sourceds = gdal.Open(fih, gdal.GA_ReadOnly)
    tpe = sourceds.GetDriver().ShortName
    if tpe == 'HDF4' or tpe == 'netCDF':
        sourceds = gdal.Open(sourceds.GetSubDatasets()[subdataset][0])
    ndv = sourceds.GetRasterBand(1).GetNoDataValue()
    xsize = sourceds.RasterXSize
    ysize = sourceds.RasterYSize
    geot = sourceds.GetGeoTransform()
    projection = osr.SpatialReference()
    projection.ImportFromWkt(sourceds.GetProjectionRef())
    driver = gdal.GetDriverByName(tpe)
    return driver, ndv, xsize, ysize, geot, projection

get_geoinfo('LandCover_35MPT.tif', subdataset=0)



