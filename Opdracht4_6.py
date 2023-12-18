# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:29:37 2023

@author: hendr
"""

import os
from osgeo import gdal, osr
import matplotlib.pyplot as plt
import numpy as np
import glob


for filename in glob.glob('*.tif'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        basename = filename.split(".tif") [0]
        dataset = gdal.Open(filename)
        band1 = dataset.GetRasterBand(1)
        b1 = band1.ReadAsArray()
        img = np.dstack((b1, ))
        q = plt.figure()
        plt.imshow(img)
        plt.savefig(basename+'.jpg', dpi=600)



