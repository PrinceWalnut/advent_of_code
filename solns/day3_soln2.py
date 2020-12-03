import numpy as np
from IPython import embed

tree_map = np.loadtxt('../data/day3_prob1.csv', comments='bruh', dtype=str)
row_length = len(tree_map[0])

dx_arr = np.asarray([1, 3, 5, 7, 1])
dy_arr = np.asarray([1, 1, 1, 1, 2])
trees_arr = np.zeros(len(dx_arr))

for i in np.arange(len(dx_arr)):
    # Position markers
    x = 0
    y = 0
    
    # Velocity markers
    dx = dx_arr[i]
    dy = dy_arr[i]
    
    # Fuckin trees
    trees = 0
    
    # Move n shit
    while y < len(tree_map):
        if tree_map[y][x] == '#':
            trees += 1
        x = (x+dx) % row_length
        y = y+dy
    trees_arr[i] = trees

print(np.product(trees_arr))
