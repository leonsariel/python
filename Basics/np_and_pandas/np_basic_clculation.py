# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 5:14 PM'

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([0, 1, 2, 3])

# matrix minus
print(a - b)
print(a + b)
print(b ** 2)

# sin cosin and tan
c = np.sin(a)
d = np.cos(a)
e = np.tan(a)
print(c, d, e)

# find elements less than 3 return: boolean
print(b < 3)

# matrix operation
a = np.array([[1, 1],
              [0, 1]])
b = np.arange(4).reshape((2, 2))
print(a)
print(b)

# normal multiply
c = a * b
print(c)

# matrix multiply
c_dot = np.dot(a, b)
print(c_dot)

# another way to do matrix multiply
c_dot2 = a.dot(b)
print(c_dot2)

# create random and find value in entire arrary
a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))

#find within axis, axis=0 is in row, axis=1 in cols
print(np.sum(a, axis=1))