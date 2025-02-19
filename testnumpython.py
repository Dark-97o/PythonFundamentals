# This file is created to test the numpy and math libraries in Python.
# The math library is used for mathematical operations and the numpy library is used for numerical operations

import math
import numpy as np
print(math.ceil(12.9))
print(math.floor(10.1))
print (math.fabs(686.798))
print (math.factorial(9))
print (math.frexp(878))
print (math.isnan (float(78.9)))

arr = np.array([34,2,65,23])
print("NumPy Array:", arr)
print("Sum of Array:", np.sum(arr))
print("Mean of Array:", np.mean(arr))
print("Maximum Value:", np.max(arr))
print("Index of Max Value:", np.argmax(arr))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nNumPy 2D Array (Matrix):\n", matrix)
transpose_matrix = np.transpose(matrix)
print("Transposed Matrix:\n", transpose_matrix)
squared_matrix = matrix ** 2
print("Squared Matrix:\n", squared_matrix)
result_matrix = np.matmul(matrix, transpose_matrix)
print("Matrix Multiplication Result:\n", result_matrix)