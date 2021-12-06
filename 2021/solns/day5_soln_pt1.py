# Advent of Code Day 5

# Imports
import numpy as np
import pandas as pd

# Get data
file = open('../data/day5_data.txt')
coords = pd.read_table(file, names=['x1','y1','x2','y2'], comment='\n', sep='\D+')

# Filter out any non-horizontal/vertical lines
coords = coords[[a or b for a,b in zip(coords['x1'] == coords['x2'], coords['y1'] == coords['y2'])]].reset_index()

# Reorient all lines to left->right or top->down directions
temp_arr = np.asarray(coords[['x1','x2']])
temp = 0
for i in range(len(temp_arr)):
    if temp_arr[i][0] > temp_arr[i][1]:
        temp = temp_arr[i][0]
        temp_arr[i][0] = temp_arr[i][1]
        temp_arr[i][1] = temp
coords[['x1','x2']] = temp_arr
temp_arr = np.asarray(coords[['y1','y2']])
temp = 0
for i in range(len(temp_arr)):
    if temp_arr[i][0] > temp_arr[i][1]:
        temp = temp_arr[i][0]
        temp_arr[i][0] = temp_arr[i][1]
        temp_arr[i][1] = temp
coords[['y1','y2']] = temp_arr

# Get boundaries of board
xmin = min(min(coords['x1']), min(coords['x2']))
xmax = max(max(coords['x1']), max(coords['x2']))
ymin = min(min(coords['y1']), min(coords['y2']))
ymax = max(max(coords['y1']), max(coords['y2']))

# Initialize board to zeros
board = np.zeros(shape=(xmax-xmin, ymax-ymin), dtype=int)

# Transform all lines to put top-left of board as (0,0)
coords['x1'] = coords['x1'] - xmin
coords['x2'] = coords['x2'] - xmin
coords['y1'] = coords['y1'] - ymin
coords['y2'] = coords['y2'] - ymin

"""
NOTE TO ANYONE READING THIS:

This solution is shit lol. You should use a sparse matrix instead of
iterating through lines per spot on board. But I'm too lazy to fix this.
"""
# Increment position values for each line they're in
for i in range(xmax-xmin):
    for j in range(ymax-ymin):
        idx = [a and b for a,b in zip(i >= coords['x1'],  i <= coords['x2'])]
        idy = [a and b for a,b in zip(j >= coords['y1'],  j <= coords['y2'])]
        id2 = [a and b for a,b in zip(idx, idy)]
        board[i][j] = sum(id2)
        print(f'({i},{j}) {sum(id2)}')

# Get number of points with multiple lines
num_intersections = sum(board.flatten() > 1)
print(num_intersections)
