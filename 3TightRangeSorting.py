import time
import os
import glob
import pandas as pd
from datetime import datetime
import numpy as np

dict = {}
stocks = pd.read_csv('stocklist.csv')
df = pd.DataFrame(stocks)
df = df.iloc[: , 1:]
arr = df["0"].to_numpy()
y = 26
# print(arr)
for stock in arr:

    df = pd.read_csv(f'filesForToday/{stock}.csv')
    df = pd.DataFrame(df)
    
    minhigh = df.iloc[0+y]['h']
    minlow = df.iloc[0+y]['l']
    rangee = (minhigh-minlow)/minhigh*100
    stock = stock+","
    dict[stock] = rangee

a = sorted(dict.items(), key=lambda x: x[1])
# print(a) 
a = pd.DataFrame(a)
a.to_csv('stocksToTrade.csv')  