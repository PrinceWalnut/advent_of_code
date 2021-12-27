# Advent of Code Day 8

# Imports
import numpy as np
import pandas as pd

# Get data
file = open('../data/day8_data.txt')
table = pd.read_table(file, header=None, sep=' ')
num_strs = np.asarray(table[[11, 12, 13, 14]], dtype=str).flatten()

# Get subset of key numbers to look for in string lengths
key_nums = [2, 4, 3, 7]

# Find how many numbers are in the subset of interest
total = 0
for i in num_strs:
    if len(i) in key_nums:
        total = total + 1

# Print result
print(total)

##### PART 2 ######

# Reshape data to look like rows
num_strs = num_strs.reshape((200,4))
test_nums = np.asarray(table[range(10)], dtype=str)
total = 0

# Pre-sort all strings in alphabetical order
for i in range(len(num_strs)):
    for j in range(4):
        num_strs[i][j] = ''.join(sorted(num_strs[i][j]))
for i in range(len(test_nums)):
    for j in range(10):
        test_nums[i][j] = ''.join(sorted(test_nums[i][j]))

# Find key for each row and decode
for i in range(len(test_nums)):
    keys = ['']*10
    str_lens = np.zeros(10)
    for j in range(10):
        str_lens[j] = len(test_nums[i][j])
    # Get 1, 4, 7, 8 keys
    keys[1] = test_nums[i][str_lens == 2][0]
    keys[4] = test_nums[i][str_lens == 4][0]
    keys[7] = test_nums[i][str_lens == 3][0]
    keys[8] = test_nums[i][str_lens == 7][0]
    # Solve keys for 5-length numbers 2, 3, 5
    for j in test_nums[i][str_lens == 5]:
        # 3 shares all of 1
        if len(set(keys[1]).intersection(j)) == 2:
            keys[3] = j
        # 5 shares 3 of 4, 2 only shares 2
        elif len(set(keys[4]).intersection(j)) == 3:
            keys[5] = j
        else:
            keys[2] = j
    # Solve keys for 6-length numbers 0, 6, 9
    for j in test_nums[i][str_lens == 6]:
        # 9 shares all of 4
        if len(set(keys[4]).intersection(j)) == 4:
            keys[9] = j
        # 0 shares 2 of 1, 6 only shares 1
        elif len(set(keys[1]).intersection(j)) == 2:
            keys[0] = j
        else:
            keys[6] = j
    # Now decode number based on keys
    str_num = ''
    for j in range(4):
        str_num = str_num + str(keys.index(num_strs[i][j]))
    # Cast to integer and add to running total
    display_num = int(str_num)
    total = total + display_num

print(total)
