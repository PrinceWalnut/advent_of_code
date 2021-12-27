# Advent of Code Day 7

# Imports
import numpy as np

# Get data
pos = np.loadtxt('../data/day7_data.txt', delimiter=',', dtype=int)
locs = np.arange(np.min(pos), np.max(pos), dtype=int)
cost = np.zeros(len(locs))

# Get fuel cost at each location
for i, x in enumerate(locs):
    fuel = 0
    for y in pos:
        fuel = fuel + np.abs(y-x)
    cost[i] = fuel

# Get minimal fuel
print(np.min(cost))

##### PART 2 #####

# Get fuel cost at each location with new function
for i, x in enumerate(locs):
    fuel = 0
    for y in pos:
        fuel = fuel + np.sum(np.arange(np.abs(y-x)+1))
    cost[i] = fuel

# Get minimal fuel
print(np.min(cost))

