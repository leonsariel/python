# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 5:59 PM'
import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# combination
print(np.vstack([A,B]))  # verticall combine A and B  out put: [[1,1,1], [2,2,2]]
print(np.hstack([A,B]))  # horizontal combine output  [1,1,1,2,2,2]

# transform [1,1,1] to [[1],[1],[1]]
print(A[:,np.newaxis])

# combine multiple matrix with axis
C = np.concatenate((A,B,B,A),axis=0)

