#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:22:03 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

gridLength = 50
maxTime = 1000000
beta = 0.2

latticePlot = np.zeros((4, gridLength, gridLength))

class Lattice():
    def __init__(self, gridLength, maxTime, beta):
        self.gridLength = gridLength
        self.maxTime = maxTime
        self.beta = beta
        
        self.lattice = np.zeros((gridLength, gridLength))
        
    def GetEnergy(self, x, y):
        thisSpin = self.lattice[x, y]
        
        topSpin = self.lattice[x, y-1] if y != 0 else 0
        bottomSpin = self.lattice[x, y+1] if y != gridLength-1 else 0
        leftSpin = self.lattice[x-1, y] if x != 0 else 0
        rightSpin = self.lattice[x+1, y] if x != gridLength-1 else 0
        
        neighbours = [topSpin, bottomSpin, leftSpin, rightSpin]
        energy = 0
        
        for neighbouringSpin in neighbours:
            energy -= thisSpin * neighbouringSpin
        
        return energy
    
    def GetTotalEnergy(self):
        totEnergy = 0
        for x in range(0, gridLength):
            for y in range(0, gridLength):
                totEnergy += self.GetEnergy(x, y)
        return totEnergy
    
    def CalcMag(self):
        return np.sum(self.lattice)

    def Metropolis(self, lattice):
        totEnergyVals = np.zeros(maxTime-1)
        totSpinVals = np.zeros(maxTime-1)
        for t in range(0, maxTime-1):
            # Pick a random particle to flip
            x = np.random.randint(0, gridLength)
            y = np.random.randint(0, gridLength)
            initialSpin = self.lattice[x, y]
            proposedSpin = initialSpin * -1
            
            energy = self.GetEnergy(x, y)
            
            # Calculate Initial Energy
            initialEnergy = 0
            initialEnergy += -initialSpin * self.lattice[x, y-1] if y != 0 else 0
            initialEnergy += -initialSpin * self.lattice[x, y+1] if y != gridLength-1 else 0
            initialEnergy += -initialSpin * self.lattice[x-1, y] if x != 0 else 0
            initialEnergy += -initialSpin * self.lattice[x+1, y] if x != gridLength-1 else 0
            
            # Calculate Final Energy
            finalEnergy = 0
            finalEnergy += -proposedSpin * self.lattice[x, y-1] if y != 0 else 0
            finalEnergy += -proposedSpin * self.lattice[x, y+1] if y != gridLength-1 else 0
            finalEnergy += -proposedSpin * self.lattice[x-1, y] if x != 0 else 0
            finalEnergy += -proposedSpin * self.lattice[x+1, y] if x != gridLength-1 else 0
            
            dE = finalEnergy - initialEnergy
            if (dE > 0) * (np.exp(-beta * (finalEnergy - initialEnergy)) > np.random.random()):
                self.lattice[x,y] = proposedSpin # Accept the proposed state!
                energy += dE
                
            elif dE <= 0:
                self.lattice[x,y] = proposedSpin # Accept the proposed state!
                energy += dE
                
            totEnergyVals[t] = energy
            totSpinVals[t] = self.CalcMag()
            
            if t == 0:
                latticePlot[0] = self.lattice
            elif t == int(maxTime/4):
                latticePlot[1] = self.lattice
            elif t == int(maxTime/2):
                latticePlot[2] = self.lattice
            elif t == int(3 * maxTime / 4):
                latticePlot[3] = self.lattice
                
        return totEnergyVals, totSpinVals
            

# Initialise lattice structure
lattice = Lattice(50, 10000, 0.2)
randomArray = np.random.random((gridLength, gridLength))
lattice.lattice[randomArray >= 0.5] = 1
lattice.lattice[randomArray < 0.5] = -1

print(f'Total Energy at time t=0: {lattice.GetTotalEnergy()} J')
print(f'Total Magnetisation at time t=0: {lattice.CalcMag()}')

totEnergyVals, totSpinVals = lattice.Metropolis(lattice)

print(f'Total Energy at time t={maxTime}: {lattice.GetTotalEnergy()} J')
print(f'Total Magnetisation at time t={maxTime}: {lattice.CalcMag()}')

fig, axes = plt.subplots(1, 2, figsize=(12,4))
ax = axes[0]
ax.plot(totSpinVals/gridLength**2)
ax.set_xlabel('Algorithm Time Steps')
ax.set_ylabel(r'Average Spin $\bar{m}$')
ax = axes[1]
ax.plot(totEnergyVals)
ax.set_xlabel('Algorithm Time Steps')
ax.set_ylabel(r'Energy $E/J$')
ax.grid()
fig.tight_layout()
fig.suptitle(r'Evolution of Average Spin and Energy for $\beta J=$1')
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(5,5), gridspec_kw={'height_ratios': [1, 1]}, subplot_kw={'xticks': [], 'yticks': []})
axes[0][0].imshow(latticePlot[0], cmap="bwr")
axes[0][1].imshow(latticePlot[1], cmap="bwr")
axes[1][0].imshow(latticePlot[2], cmap="bwr")
axes[1][1].imshow(latticePlot[3], cmap="bwr")
plt.show()
