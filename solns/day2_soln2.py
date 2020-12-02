import numpy as np
import pandas as pd
from IPython import embed

data = pd.read_csv('../data/day2_prob1.csv', delimiter=' ', names=['Rule', 'Letter', 'Password'])
data['Rule'] = data['Rule'].str.split('-')
data['Letter'] = data['Letter'].str[0]
data['Valid'] = data.apply( lambda x: (x.Password[int(x.Rule[0]) - 1] == x.Letter) ^ (x.Password[int(x.Rule[1]) - 1] == x.Letter), axis=1)
print(sum(data['Valid']))
