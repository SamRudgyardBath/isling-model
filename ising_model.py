#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:22:03 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

gridLength = 100

def GetEnergy(x, y):
    thisSpin = lattice[x, y]
    
    topSpin = lattice[x, y - 1] if y != 0 else 0
    bottomSpin = lattice[x, y + 1] if y != gridLength-1 else 0
    leftSpin = lattice[x - 1, y] if x != 0 else 0
    rightSpin = lattice[x + 1, y] if x != gridLength-1 else 0
    
    neighbours = [topSpin, bottomSpin, leftSpin, rightSpin]
    energy = 0
    
    for neighbouringSpin in neighbours:
        energy -= thisSpin * neighbouringSpin
    
    return energy

def GetTotalEnergy():
    totEnergy = 0
    for x in range(0, gridLength):
        for y in range(0, gridLength):
            totEnergy += GetEnergy(x, y)
    return totEnergy

# Initialise lattice structure
lattice = np.zeros((gridLength, gridLength)) 
randomArray = np.random.random((gridLength, gridLength))
lattice[randomArray >= 0.75] = 1
lattice[randomArray < 0.75] = -1

print(f'Total Energy: {GetTotalEnergy()} J')
plt.imshow(lattice)
