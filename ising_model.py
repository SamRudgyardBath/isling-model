#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:22:03 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

gridLength = 100
# Initialise lattice structure
lattice = np.zeros((gridLength, gridLength)) 
randomArray = np.random.random((gridLength, gridLength))
lattice[randomArray >= 0.75] = 1
lattice[randomArray < 0.75] = -1

plt.imshow(lattice)
