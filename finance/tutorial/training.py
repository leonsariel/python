# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/15/2018 6:59 PM'
from sklearn import svm, preprocessing
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
import time
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


def build_data_set():

    print("hello program started!")
    data = pd.read_csv("data/master_frame.csv")
    feature_list = [i for i in data]
    feature_list = feature_list[1:-6]

    # set first row as the column names
    data.rename(columns=data.iloc[0])
    data = data.set_index(pd.to_datetime(data.Date))
    del data['Date']
    print(len(data))
    data = data[:2000]

    X = np.array(data[feature_list].values)
    y = (data["status"].values.tolist())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # normalize the data
    X = preprocessing.scale(X)

    return X_train, X_test, y_train, y_test


def analysis():


    X_train, X_test, y_train, y_test = build_data_set()
    clf = svm.SVC( kernel="linear", C=1 , verbose=True)
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'svm_model.pkl')
    prediction = clf.predict(X_test)
    correct_count = 0
    for x in range(0, len(y_test)):
        print(prediction)
        if prediction[x] == y_test[x]:
            correct_count += 1

        # if clf.predict(X[-x])[0] == y[-x]:
        #         correct_count += 1
    print("Accuracy is: ", (correct_count / len(y_test)) * 100)
    end = time.time()
    print("total time: ",end - start)
    result = clf.score(X_test, y_test)
    print(result)

start = time.time()
analysis()


