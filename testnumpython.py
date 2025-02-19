import math
import numpy as np
print(math.ceil(12.9))
print(math.floor(10.1))
print (math.fabs(686.9787998))
print (math.factorial(9))
print (math.frexp(878))
print (math.isnan (float(78.9)))
print (math.isnan (math.nan))
print (math.isnan (math.inf))

arr = np.array([34,2,65,23])
print("NumPy Array:", arr)
print("Sum of Array:", np.sum(arr))
print("Mean of Array:", np.mean(arr))
print("Maximum Value:", np.max(arr))
print("Index of Maximum Value:", np.argmax(arr))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nNumPy 2D Array (Matrix):\n", matrix)
transpose_matrix = np.transpose(matrix)
print("Transposed Matrix:\n", transpose_matrix)
squared_matrix = matrix ** 2
print("Squared Matrix:\n", squared_matrix)
result_matrix = np.matmul(matrix, transpose_matrix)
print("Matrix Multiplication Result:\n", result_matrix)