# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:03:46 2024

@author: hendr
"""

import os

from Ex7 import area_df

area_df.to_excel(os.path.join("OUT", "area_table.xlsx"))
area_df.to_csv(os.path.join("OUT", "area_table.csv"))