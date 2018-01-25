# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/22/2018 3:25 PM'

from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from sklearn.externals import joblib


print("hello program started!")
data = pd.read_csv("data/master_frame2.csv")
feature_list = [i for i in data]
feature_list = feature_list[1:-6]

# set first row as the column names
data.rename(columns=data.iloc[0])
data = data.set_index(pd.to_datetime(data.Date))
del data['Date']
print(len(data))
# data = data[4000:6010]

X = np.array(data[feature_list].values)
y = (data["status"].values.tolist())

X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = joblib.load('svm_model.pkl')
prediction = clf.predict(X_test)
result = clf.score(X_test, y_test)
print(y_test)
print(prediction)
print(result)