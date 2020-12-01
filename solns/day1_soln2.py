import numpy as np
import pandas as pd

data = pd.read_csv('../data/day1_prob1.csv', names=['input'])

input_data = data['input'].to_numpy()
soln_found = False

for i in input_data:
    for j in input_data:
        for k in input_data:
            if i+j+k == 2020:
                print(i*j*k)
                soln_found=True
                break
        if(soln_found):
            break
    if(soln_found):
        break
