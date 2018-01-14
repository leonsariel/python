# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 4:36 PM'

import pandas as pd
import numpy as np
from tutorial.feature_functions import *

#load our data

data = pd.read_csv('data/EURUSD_hours.csv')
data.columns = [['Date','open','high','low','close','AskVol']]
data = data.set_index(pd.to_datetime(data.Date))
data.columns = [['open','high','low','close','AskVol']]
prices = data.drop_duplicates(keep=False)

#create lists for each period required by our functions

# momentum_key = [i for i in range(3,11)]
# print(momentum_key)