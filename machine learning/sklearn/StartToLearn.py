# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/1/2018 12:52 PM'

from sklearn.cross_validation import train_test_split

# auto learning process
#  x: features, y: label,
# testSize: test size vs population 0-1,
# classifier: object of classifier eg: knn = KNeighborsClassifer()

def startToLearn(x, y, testSize, classifier):
    # split data
    trainX, testX, trainY, testY = train_test_split(x, y, test_size=testSize)

    #fit to model
    classifier.fit(trainX,trainY)
    score = classifier.score(testX,testY)
    print("prediction from test dataset: ", classifier.predict(testX))
    print("Actual result from test dataset: ", testY)
    print("Score from 0 to 1: ", score)
    return classifier.predict(testX), testY, score