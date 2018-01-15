# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 7:54 PM'
import pandas as pd
import numpy as np

#read csv
data = pd.read_csv('student.csv')
print(data)

# save to pickle(file type)
data.to_pickle('student.pickle')