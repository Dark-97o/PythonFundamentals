import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target
print(df)

# data = { 'Name': ['Subhranil','Abhishek'],
#         'Age':[30,46],
#         'State':['Jharkhand','Bihar']}

# df = pd.DataFrame(data)
# print(df)
# print(df['Name'])
# print(df.Age)
# df['Salary']=[10,20]
# # print(df)
# # print(df.loc[1])
# print(df.describe())



# sr = pd.Series([1,2,3,4,5])
# print(sr)
# print(sr.index)
# print(sr.values)

# arr = np.array([1,2,3,4,5])
# compare = sr == arr
# print(compare)

# sr2 = pd.Series([1,2,3], index = ['A','B','C'])
# print(sr2.index)
# print(sr2)
# print(sr2['B'])



# df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
# print(df)

