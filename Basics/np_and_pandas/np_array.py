# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 4:58 PM'

import numpy as np

# set default type for np array eg np.int64, np.float
a = np.array([12, 2323, 12], dtype=np.int)
print(a.dtype)

# set multi-line matrix
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# zero matrix with 3 rows and 4 col
zero = np.zeros((3, 4))
print(zero)

# create ones in matrix
one = np.ones((3, 4))
print(one)

# create ordered number list like range, from 10 to 19, step is 2
order_list = np.arange(10, 20, 2)
print(order_list)

# create order number list from 0 to 11, then make it as 3 row 4 cols
order_list2 = np.arange(12).reshape((3, 4))
print(order_list2)

# create line from 1 to 10 divide into 5 dots
line = np.linspace(1, 10, 5)
print(line)
