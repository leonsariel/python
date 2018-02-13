# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '2/2/2018 6:12 PM'
import pandas as pd
import numpy as np
import talib

close = np.random.random(20)
print(close)

# Simple Moving Average with 5 interval,  averge of first 5 and put in 5th position
# [        nan         nan         nan         nan  0.31820338  0.22168435 .....
#  0.3330296   0.38871325  0.38913524  0.40332351  0.59535573  0.43606699
#  0.35442881  0.40883881  0.38270418  0.34287136  0.44672772  0.37151548]
def print_SMA(close):
    output = talib.SMA(close, 5)
    print(output)
