# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:12:49 2019

Creates a grid of size NxN. Each square created within the grid will not have 
4 identical vertices.
"""

import numpy as np
import time

# create random grid
def createRandGrid(size):
    grid = np.random.random([size,size])
    grid = np.rint(grid)
    return grid

# returns True if the grid is valid, False otherwise
def checkGrid(grid):
    valid = True
    size = len(grid)
    for i in range(size):
        for j in range(size):
            stepRange = size-max([i,j])
            for step in range(1,stepRange):
                topLeft = grid[i][j]
                topRight = grid[i+step][j]
                bottomLeft = grid[i][j+step]
                bottomRight = grid[i+step][j+step]
                if topLeft == topRight and topLeft == bottomLeft and topLeft == bottomRight:
                    valid = False
    return valid

# change a random element of the grid
def changeGrid(grid):
    size = len(grid)
    i = np.random.randint(0,size)
    j = np.random.randint(0,size)
    if grid[i][j] == 0:
        grid[i][j] = 1
    else:
        grid[i][j] = 0
    return grid

# create a valid grid
def createValidGrid(size):
    grid = createRandGrid(size)
    startTime = time.time()
    valid = False
    iterations = 0
    while valid == False:
        iterations += 1
        grid = changeGrid(grid)
        valid = checkGrid(grid)
    return grid, iterations, time.time() - startTime