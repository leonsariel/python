# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 5:31 PM'
import numpy as np

A = np.arange(2,14).reshape((3,4))
print(A)

# find index of min, max mean
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))
# Same as abover
print(A.mean())

#find median
print(np.median(A))

#cumulate sum
np.cumsum(A)

#find difference between first and second elements
np.diff(A)

# find non zero
np.nonzero(A)

# sort by row, not entire
np.sort(A)

# tanspose
np.transpose(A)
A.T   #same

# clip natrix any elements lower than 5 equals to 5, larger than 9 equals to 9
np.clip(A,5,9)

A = np.arange(3,15).reshape((3,4))
print(A)
# print element with index
A[2]
# print all elements in row 3
print(A[2, :])

# print all elements in cols 0
print(A[:,0])

# for loop get row
for row in A:
    print(A)

# for to get cols
for col in A.T:
    print(col)

# transform matrix into one single list flatten and flat
print(A.flatten())
for item in A.flat:
    print(item)