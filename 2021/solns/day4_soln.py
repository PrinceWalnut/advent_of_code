# Advent of Code Day 4

# Imports
import numpy as np
import re

# Get data
bingo = open('../data/day4_data.txt')

# Get numbers in order
nums = bingo.readline().rstrip('\n').split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Get board data
bingo.readline() # Flush empty line
data = bingo.readlines()

# Strip newlines and empty lines
data = np.asarray([i.rstrip('\n') for i in data])
data = data[data != '']

# Split into individual boards and store in list
boards = []
for i in range(0,len(data),5):
    board = data[i:i+5]
    board_arr = np.zeros(shape=(5,5), dtype=int)
    for j in range(len(board)):
        board_arr[j] = np.asarray(re.split(' +', board[j].lstrip(' ')), dtype=int)
    boards.append(board_arr)

# For each board, determine when it would win
win_indices = []
for board in boards:
    idw = np.inf
    # Check win index for each row and store earliest
    for i in range(5):
        if max([nums.index(j) for j in board[i]]) < idw:
            idw = max([nums.index(j)for j in board[i]])
    # Check win index for each column and store earliest (if earlier than row win)
    for i in range(5):
        if max([nums.index(j) for j in board[:,i]]) < idw:
            idw = max([nums.index(j)for j in board[:,i]])

    # Store when this board would win
    win_indices.append(idw)

# Select first winning board and calculate score
board_win = boards[win_indices.index(min(win_indices))].flatten()
multiplier = nums[min(win_indices)]
taken_nums = nums[:min(win_indices)+1]
score = multiplier*sum(board_win[[i not in taken_nums for i in board_win]])
print(score)

##### PART 2 ######

# Last win is trivial, just take the maximums of the above calculations instead
board_win = boards[win_indices.index(max(win_indices))].flatten()
multiplier = nums[max(win_indices)]
taken_nums = nums[:max(win_indices)+1]
score = multiplier*sum(board_win[[i not in taken_nums for i in board_win]])
print(score)
