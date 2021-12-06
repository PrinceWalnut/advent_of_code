# Advent of Code Day 6

"""
To solve Part 2, simply change days_orig = 256
"""

# Imports
import numpy as np

# Get data
fish = np.loadtxt('../data/day6_data.txt', delimiter=',', dtype=int)

# Get number of fish in each countdown bin
coeff = np.zeros(7, dtype=int)
for i in range(7):
    coeff[i] = sum(fish == i)

# Set time length
days_orig = 80

# Calculate additional fish per countdown bin
spawn = np.zeros(7, dtype=int)
for i in range(7):
    # Set countdowns
    countdowns = np.zeros(9, dtype=int)
    countdowns[i] = 1
    temp = 0
    days = days_orig
    while(days > 0): # Iterate through days
        days = days - 1
        temp = countdowns[0]
        for j in range(len(countdowns) - 1):
            countdowns[j] = countdowns[j+1]
        countdowns[-3] = countdowns[-3] + temp # Adults cycle
        countdowns[-1] = temp # Children cycle
    spawn[i] = sum(countdowns)

# Calculate total fish
tot_fish = 0
for i in range(7):
    tot_fish = tot_fish + spawn[i]*coeff[i]
print(tot_fish)
