# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/15/2018 7:15 PM'
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100)
x, y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)
data = digits.data[-1].reshape(1, -1)
print('prediciton',clf.predict(data))

plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

a = 'asdfasdfasdf'
print(a[:-2])