# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/1/2018 2:05 PM'

from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt


iris = load_iris()
x = iris.data
y = iris.target

trainX, testX, trainY, testY = train_test_split(x,y, random_state = 4)

# use 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
# divided by 5 groups
score = cross_val_score(knn, x, y, cv=5, scoring='accuracy')
# print(score.mean())


# iterate through k different neighbor to find the best fit
def findBestKNN(x,y, k):
    k_range = range(1,k+1)
    k_scores = []
    for i in k_range:
        knn = KNeighborsClassifier(n_neighbors=i)
        scores = cross_val_score(knn, x, y, cv=10, scoring='accuracy')
        k_scores.append(scores.mean())

    plt.plot(k_range, k_scores)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Cross Validated Accuracy')
    plt.show()

findBestKNN(x,y,30)
