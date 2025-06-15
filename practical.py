import numpy as np
from scipy import linalg
import pandas as pd

# data = np.random.randn(100)
# array1 = np.array([data])

# array1 = np.array([23,32,76,54,90])
# print("Original Array: ",array1)
# maxi = np.argmax(array1)
# mini = np.argmin(array1)
# max1 = np.max(array1)
# min1 = np.min(array1)
# array1[maxi] = min1
# array1[mini] = max1
# print("Changed Array: ",array1)

array2 = np.array([[34,2,32],[4,59,6],[76,88,9]])
determinant = linalg.det(array2)
print("Determinant of Array: ")
print(array2)
print("is",determinant)


# data = [100,200,'python',300.12,400]
# df = pd.Series(data)
# print("Original Data Series: \n",df)
# array1 = np.array(df)
# print("Series to an Array: \n",array1)
