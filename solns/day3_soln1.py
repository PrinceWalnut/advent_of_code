import numpy as np
from IPython import embed

tree_map = np.loadtxt('../data/day3_prob1.csv', comments='bruh', dtype=str)
row_length = len(tree_map[0])

# Position markers
x = 0
y = 0

# Velocity markers
dx = 3
dy = 1

# Fuckin trees
trees = 0

# Move n shit
while y < len(tree_map):
    if tree_map[y][x] == '#':
        trees += 1
    x = (x+dx) % row_length
    y = y+dy

print(trees)
