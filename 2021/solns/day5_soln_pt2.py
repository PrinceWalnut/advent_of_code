# Advent of Code Day 5

# Imports
import numpy as np
import pandas as pd

# Get data
file = open('../data/day5_data.txt')
coords = pd.read_table(file, names=['x1','y1','x2','y2'], comment='\n', sep='\D+')

# Get boundaries of board
xmin = min(min(coords['x1']), min(coords['x2']))
xmax = max(max(coords['x1']), max(coords['x2'])) + 1
ymin = min(min(coords['y1']), min(coords['y2']))
ymax = max(max(coords['y1']), max(coords['y2'])) + 1

# Initialize board to zeros
board = np.zeros(shape=(xmax-xmin, ymax-ymin), dtype=int)

# Transform all lines to put top-left of board as (0,0)
coords['x1'] = coords['x1'] - xmin
coords['x2'] = coords['x2'] - xmin
coords['y1'] = coords['y1'] - ymin
coords['y2'] = coords['y2'] - ymin

# Split into horiz, vert, and diag
horiz = coords[coords['y1'] == coords['y2']].reset_index(drop=True)
vert = coords[coords['x1'] == coords['x2']].reset_index(drop=True)
diag = pd.concat([coords, horiz, vert]).drop_duplicates(keep=False)

# Make horiz lines left->right
# Reorient all lines to left->right or top->down directions
temp_arr = np.asarray(horiz[['x1','x2']])
temp = 0
for i in range(len(temp_arr)):
    if temp_arr[i][0] > temp_arr[i][1]:
        temp = temp_arr[i][0]
        temp_arr[i][0] = temp_arr[i][1]
        temp_arr[i][1] = temp
horiz[['x1','x2']] = temp_arr

# Make vertical lines top->down
temp_arr = np.asarray(vert[['y1','y2']])
temp = 0
for i in range(len(temp_arr)):
    if temp_arr[i][0] > temp_arr[i][1]:
        temp = temp_arr[i][0]
        temp_arr[i][0] = temp_arr[i][1]
        temp_arr[i][1] = temp
vert[['y1','y2']] = temp_arr

# Increment all spots in a horizontal line
for row in horiz.iterrows():
    for i in range(row[1][0], row[1][2]+1): # Scan across line
        board[row[1][1]][i] = board[row[1][1]][i] + 1

# Increment all spots in a vertical line
for row in vert.iterrows():
    for i in range(row[1][1], row[1][3]+1): # Scan across line
        board[i][row[1][0]] = board[i][row[1][0]] + 1

# Increment all spots in a diagonal line
for row in diag.iterrows():
    mag = abs(row[1][2] - row[1][0]) + 1 # Length of line
    for i in range(mag):
        if row[1][2] - row[1][0] > 0:
            if row[1][3] - row[1][1] > 0: # right + down
                board[row[1][1] + i][row[1][0] + i] = board[row[1][1] + i][row[1][0] + i]  + 1
            else: #right + up
                board[row[1][1] - i][row[1][0] + i] = board[row[1][1] - i][row[1][0] + i]  + 1
        else:
            if row[1][3] - row[1][1] > 0: # left + down
                board[row[1][1] + i][row[1][0] - i] = board[row[1][1] + i][row[1][0] - i]  + 1
            else: # left + up
                board[row[1][1] - i][row[1][0] - i] = board[row[1][1] - i][row[1][0] - i]  + 1

# Get number of points with multiple lines
num_intersections = sum(board.flatten() > 1)
print(num_intersections)


