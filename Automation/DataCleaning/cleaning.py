import numpy as nm
import json
import pandas as pd

import pymongo

DATA = pd.read_csv('./all.csv')


# print(DATA.iloc[:50])

OPrice = pd.read_csv('./all.csv')
h = []
for i in range(50):
    if str(OPrice.iloc[i,5])[:2] == 'na':
        h.append(0)
    else:
        h.append(int(str(OPrice.iloc[i,5])[:2]))

print(h)