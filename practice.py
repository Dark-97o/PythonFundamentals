import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize,stats,linalg

# np.random.seed(0)
# data1 = np.random.randn(500)
# from sklearn.datasets import load_iris

# iris = load_iris()
# df = pd.DataFrame(data=iris.data, columns = iris.feature_names)
# df['target'] = iris.target
# print(df)

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

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]
# Categories = ['A','B','C','D']
# values = [20,30,25,35]

# plt.subplot(1,4,1)
# plt.plot(x,y)
# plt.title('Line Plot')

# plt.subplot(1,4,2)
# plt.bar(x,arr)
# plt.title('Bar Plot')

# plt.subplot(1,4,3)
# plt.scatter(Categories,values)
# plt.title('Scatter Plot')

# plt.subplot(1,4,4)
# plt.hist(data1,bins=30)
# plt.title('Histogram')

# plt.show()

# arr3 = np.array([12,2,3,4,5])
# # print(np.std(arr3))
# # print(np.argmax(arr3))

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# tarr2 = np.transpose(arr2)
# print(np.transpose(arr2))
# print(np.matmul(arr2,tarr2))
# print(tarr2**2)

# def simple(x):
#     return x**2 + x*3 + 4

# result = optimize.minimize(simple, x0=0)

# print(result)
# print()
# print(result.x)
# print()
# print(result.fun)

determ = np.linalg.det(arr2)
eigen_val,eigen_vec = np.linalg.eig(arr2)
print(determ,eigen_val,eigen_vec)