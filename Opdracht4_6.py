# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:29:37 2023

@author: hendr
"""



import os
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import osr

gdal.UseExceptions()

def get_gdalwarp_info(fih = "C:/Users/larak/OneDrive/Geografie/3e BAC/Environmental programming/Topic10_Axel_Environmental_Analysis_using_Remote_Sensing_data/DATA/Optical_images/20210830T080609_20210830T082514_T35MQS.tif", subdataset=0):
    dataset = gdal.Open(fih, gdal.GA_ReadOnly)
    tpe = dataset.GetDriver().ShortName
    if tpe == 'HDF4':
        dataset = gdal.Open(dataset.GetSubDatasets()[subdataset][0])
    ndv = str(dataset.GetRasterBand(1).GetNoDataValue())
    if ndv == 'None':
        ndv = 'nan'
    srs = dataset.GetProjectionRef()
    if not srs:
        srs = osr.SpatialReference()
        srs.ImportFromEPSG(4326).ExportToPrettyWkt()
        print("srs not defined, using EPSG4326.")
    xsize = dataset.RasterXSize
    ysize = dataset.RasterYSize
    res = ' '.join([str(xsize), str(ysize)])
    geot = dataset.GetGeoTransform()
    xmin = geot[0]
    ymin = geot[3] + geot[5] * ysize
    xmax = geot[0] + geot[1] * xsize
    ymax = geot[3]
    bbox = ' '.join([str(xmin), str(ymin), str(xmax), str(ymax)])
    return srs, res, bbox, ndv

def get_gdalwarp_info(fih = "C:/Users/larak/OneDrive/Geografie/3e BAC/Environmental programming/Topic10_Axel_Environmental_Analysis_using_Remote_Sensing_data/DATA/Optical_images/20210830T080609_20210830T082514_T35MQS.tif", subdataset=0):
    dataset = gdal.Open(fih, gdal.GA_ReadOnly)
    tpe = dataset.GetDriver().ShortName
    if tpe == 'HDF4':
        dataset = gdal.Open(dataset.GetSubDatasets()[subdataset][0])
    ndv = str(dataset.GetRasterBand(2).GetNoDataValue())
    if ndv == 'None':
        ndv = 'nan'
    srs = dataset.GetProjectionRef()
    if not srs:
        srs = osr.SpatialReference()
        srs.ImportFromEPSG(4326).ExportToPrettyWkt()
        print("srs not defined, using EPSG4326.")
    xsize = dataset.RasterXSize
    ysize = dataset.RasterYSize
    res = ' '.join([str(xsize), str(ysize)])
    geot = dataset.GetGeoTransform()
    xmin = geot[0]
    ymin = geot[3] + geot[5] * ysize
    xmax = geot[0] + geot[1] * xsize
    ymax = geot[3]
    bbox = ' '.join([str(xmin), str(ymin), str(xmax), str(ymax)])
    return srs, res, bbox, ndv

image_folder = "C:/Users/larak/OneDrive/Geografie/3e BAC/Environmental programming/Topic10_Axel_Environmental_Analysis_using_Remote_Sensing_data/DATA/Optical_images" # Replace with the actual path to your image folder
output_folder = "C:/Users/larak/OneDrive/Geografie/3e BAC/Environmental programming/Topic10_Axel_Environmental_Analysis_using_Remote_Sensing_data/DATA/Output_"  # Replace with the actual path where you want to save the output maps

for filename in os.listdir(image_folder):
    if filename.endswith(".tif"):  # Assuming images are in GeoTIFF format
        image_path = os.path.join(image_folder, filename)

def open_as_array(fih, bandnumber=1, nan_values=True):
    dataset = gdal.Open(fih, gdal.GA_ReadOnly)
    tpe = dataset.GetDriver().ShortName
    if tpe == 'HDF4':
        subdataset = gdal.Open(dataset.GetSubDatasets()[bandnumber][0])
        ndv = int(subdataset.GetMetadata()['_FillValue'])
    else:
        subdataset = dataset.GetRasterBand(bandnumber)
        ndv = subdataset.GetNoDataValue()
    array = subdataset.ReadAsArray()
    if nan_values:
        if len(array[array == ndv]) >0:
            array[array == ndv] = np.nan
    return array

def open_as_array(fih, bandnumber=2, nan_values=True):
    dataset = gdal.Open(fih, gdal.GA_ReadOnly)
    tpe = dataset.GetDriver().ShortName
    if tpe == 'HDF4':
        subdataset = gdal.Open(dataset.GetSubDatasets()[bandnumber][0])
        ndv = int(subdataset.GetMetadata()['_FillValue'])
    else:
        subdataset = dataset.GetRasterBand(bandnumber)
        ndv = subdataset.GetNoDataValue()
    array = subdataset.ReadAsArray()
    if nan_values:
        if len(array[array == ndv]) >0:
            array[array == ndv] = np.nan
    return array

fih = "C:/Users/larak/OneDrive/Documenten/GitHub/GeoGodesses_Examentaak/Topic10_Axel_Environmental_Analysis_using_Remote_Sensing_data/DATA/Optical_images/20210601T080609_20210601T082518_T35MPT.tif"

dataset = gdal.Open(fih)
red_band = dataset.GetRasterBand(1).ReadAsArray()
nir_band = dataset.GetRasterBand(2).ReadAsArray()


def calculate_ndvi(red_band, nir_band):
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

def calculate_savi(red_band, nir_band):
    savi = 1.5 * ((nir_band - red_band) / (nir_band + red_band + 0.5))
    return savi

ndvi_result = calculate_ndvi(red_band, nir_band)
savi_result = calculate_savi(red_band, nir_band)

plt.imshow(ndvi_result, cmap='YlGn', vmin=0, vmax=1)
plt.title(f"NDVI Map - {filename}")
plt.colorbar(label="NDVI Value")
plt.savefig(os.path.join(output_folder, f"ndvi_map_{filename}"))
plt.close()

plt.imshow(savi_result, cmap='YlGn', vmin=0, vmax=1)
plt.title(f"SAVI Map - {filename}")
plt.colorbar(label="SAVI Value")
plt.savefig(os.path.join(output_folder, f"savi_map_{filename}"))
plt.close()

