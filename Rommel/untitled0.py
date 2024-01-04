#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:42:15 2023

@author: lenie
"""

open('LandCover_35MPT.tif', 'r')

#hey guys 

#laraisleuk

from osgeo import gdal, osr
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy as np