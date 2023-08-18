#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:22:03 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

gridLength = 100

def GetEnergy(index):
    thisSpin = lattice[index]
    topSpin = lattice[index - gridLength]
    bottomSpin = lattice[index + gridLength]
    leftSpin = lattice[index - 1]
    rightSpin = lattice[index + 1]
    
    neighbours = [topSpin, bottomSpin, leftSpin, rightSpin]
    energy = 0
    
    for neighbouringSpin in neighbours:
        energy -= thisSpin * neighbouringSpin
    
    return energy

# Initialise lattice structure
lattice = np.zeros((gridLength, gridLength)) 
randomArray = np.random.random((gridLength, gridLength))
lattice[randomArray >= 0.75] = 1
lattice[randomArray < 0.75] = -1

plt.imshow(lattice)
