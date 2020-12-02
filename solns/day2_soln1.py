import numpy as np
import pandas as pd
from IPython import embed

data = pd.read_csv('../data/day2_prob1.csv', delimiter=' ', names=['Rule', 'Letter', 'Password'])
data['Rule'] = data['Rule'].str.split('-')
data['Letter'] = data['Letter'].str[0]
data['Total_Occurrences'] = data.apply( lambda x: x.Password.count(x.Letter), axis=1)
data['Valid'] = data.apply( lambda x: int(x.Rule[0]) <= x.Total_Occurrences <= int(x.Rule[1]), axis=1)
print(sum(data['Valid']))
