# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 7:29 PM'
import pandas as pd
import numpy as np

# init a DF
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# select column A
print(df.A)

# slice first 3 rows
print(df[0:3])

# or slice by values
print(df['20130102':'20130104'])
print("\n")

# select by label: loc
print(df.loc['20130102'])

# select only A and B columns
print(df.loc[:, ['A', 'B']])

# select only A and B in one specific row
print(df.loc['20130102', ['A', 'B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3][1])  # row 4 column 2

# select by list of row
print(df.iloc[[1, 3, 5], 1:3])

# mixed selection with index and labels ix
print(df.ix[:3, ['A', 'C']])

# Boolean index with condition check
print(df[df.A > 8])

