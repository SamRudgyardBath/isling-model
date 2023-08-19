#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:22:03 2023

@author: sam
"""

import math
import numpy as np
import matplotlib.pyplot as plt

gridLength = 100
maxTime = 100000
beta = 1

def GetEnergy(x, y):
    thisSpin = lattice[x, y]
    
    topSpin = lattice[x, y-1] if y != 0 else 0
    bottomSpin = lattice[x, y+1] if y != gridLength-1 else 0
    leftSpin = lattice[x-1, y] if x != 0 else 0
    rightSpin = lattice[x+1, y] if x != gridLength-1 else 0
    
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

def Metropolis():
    for t in range(0, maxTime):
        # Pick a random particle to flip
        x = np.random.randint(0, gridLength)
        y = np.random.randint(0, gridLength)
        initialSpin = lattice[x, y]
        proposedSpin = initialSpin * -1
        
        # Calculate Initial Energy
        initialEnergy = 0
        initialEnergy += -initialSpin * lattice[x, y-1] if y != 0 else 0
        initialEnergy += -initialSpin * lattice[x, y+1] if y != gridLength-1 else 0
        initialEnergy += -initialSpin * lattice[x-1, y] if x != 0 else 0
        initialEnergy += -initialSpin * lattice[x+1, y] if x != gridLength-1 else 0
        
        # Calculate Final Energy
        finalEnergy = 0
        finalEnergy += -proposedSpin * lattice[x, y-1] if y != 0 else 0
        finalEnergy += -proposedSpin * lattice[x, y+1] if y != gridLength-1 else 0
        finalEnergy += -proposedSpin * lattice[x-1, y] if x != 0 else 0
        finalEnergy += -proposedSpin * lattice[x+1, y] if x != gridLength-1 else 0
        
        if finalEnergy > initialEnergy:
            probOfFlip = math.exp(-beta * (finalEnergy - initialEnergy))
        else:
            probOfFlip = 1
            
        if probOfFlip >= np.random.random():
            lattice[x,y] = proposedSpin # Accept the proposed state!

# Initialise lattice structure
lattice = np.zeros((gridLength, gridLength)) 
randomArray = np.random.random((gridLength, gridLength))
lattice[randomArray >= 0.75] = 1
lattice[randomArray < 0.75] = -1

print(f'Total Energy: {GetTotalEnergy()} J')
Metropolis()
plt.imshow(lattice)
