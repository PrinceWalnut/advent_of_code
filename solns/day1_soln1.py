import pandas as pd

data = pd.read_csv('../data/day1_prob1.csv', names=['input'])
data['complement'] = 2020 - data['input']
data['correct_entry'] = data['complement'].isin(data['input'])
nums = data[data['correct_entry']==True]

print(nums['input'].prod())
