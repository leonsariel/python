# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 6:31 PM'
import numpy as np

a = np.array([1,2,3,4,5])
# get only value from a, so when a change b won't (deep copy)
b = a.copy()