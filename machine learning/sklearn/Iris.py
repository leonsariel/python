# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/1/2018 12:43 PM'

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

from StartToLearn import startToLearn

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target

knn = KNeighborsClassifier()

#return 3 value from test datasets
predict, actual, score = startToLearn(iris_x, iris_y, 0.3, knn)

# print(predict)
# print(actual)
# print(score)