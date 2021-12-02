# Advent of Code Day 1 - Part 1

# Imports
import numpy as np

# Open file
file = open('../data/day1_data.txt')

# Get depths
depths = file.readlines()
depths = [int(point.rstrip('\n')) for point in depths]

# Get increase
count = 0
for i, j in zip(depths, depths[1:]):
    if(j > i):
        count = count+1

# Profit
print(count)

##### PART 2 #####

# Reset count
count = 0
sum1 = 0
sum2 = np.inf

# Count increases
for i in range(len(depths)-2):
    sum1 = sum(depths[i:i+3])
    if(sum1 > sum2):
        count = count+1
    sum2 = sum1

# Moar profit
print(count)
