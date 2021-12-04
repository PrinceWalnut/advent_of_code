# Advent of Code Day 2

# Imports
import numpy as np
import pandas as pd

# Read file as two-column list
commands = pd.read_table('../data/day2_data.txt', delimiter=' ', names=['Directions', 'Distance'])

# Initialize position
horiz = 0
vert = 0

# Iterate through commands
for i in range(len(commands)):
    if commands['Directions'][i] == 'forward':
        horiz = horiz + commands['Distance'][i]
        continue
    if commands['Directions'][i] == 'up':
        vert = vert - commands['Distance'][i]
    else:
        vert = vert + commands['Distance'][i]

print(horiz)
print(vert)
print(horiz*vert)

##### PART 2 #####

# Reset variables
aim = 0
horiz = 0
vert = 0

# Iterate through commands
for i in range(len(commands)):
    if commands['Directions'][i] == 'forward':
        horiz = horiz + commands['Distance'][i]
        vert = vert + aim * commands['Distance'][i]
        continue
    if commands['Directions'][i] == 'up':
        aim = aim - commands['Distance'][i]
    else:
        aim = aim + commands['Distance'][i]

print(horiz)
print(vert)
print(horiz*vert)
