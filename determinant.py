import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Compute the determinant
det = np.linalg.det(matrix)

# Print the result
print(f"The determinant of the matrix:")
print(matrix)
print(f"is: {det:.2f}")  # Formatted to 2 decimal places

# Note: For a singular matrix (determinant 0), the matrix is not invertible
# This example matrix is singular (det = 0) as its rows are linearly dependent
