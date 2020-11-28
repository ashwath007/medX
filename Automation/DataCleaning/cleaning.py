import numpy as nm
import json
import pandas as pd

import pymongo

DATA = pd.read_csv('./all.csv')


# print(DATA.iloc[:50])

OPrice = pd.read_csv('./all.csv')
h = []
for i in range(100):
    l=0
    if str(OPrice.iloc[i,5])[:2] == 'na':
        h.append(0)
    else:
        l = int(str(OPrice.iloc[i,5])[:2])
        h.append(l)

for ii in range(100):
    print(OPrice.iloc[ii,4])

print(h)