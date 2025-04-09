import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# i. Create a Series using pandas and display
print("i. Creating a Series using pandas:")
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)

# ii. Access the index and the values of our Series
print("\nii. Accessing index and values:")
print("Index:", series1.index)
print("Values:", series1.values)

# iii. Compare an array using numpy with a series using pandas
print("\niii. Comparing a numpy array with a pandas Series:")
array = np.array([10, 20, 30, 40, 50])
comparison = array == series1.values
print("Numpy Array:", array)
print("Series Values:", series1.values)
print("Comparison Result:", comparison)

# iv. Define Series objects with individual indices
print("\niv. Series with custom indices:")
series2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(series2)

# v. Access single value of a series
print("\nv. Accessing single value from series:")
print("Value at index 'b':", series2['b'])

# vi. Load datasets in a dataframe variable using pandas
# We'll use a small CSV from URL for demo or simulate with sample data
print("\nvi. Loading dataset into a DataFrame:")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# vii. Usage of different methods in Matplotlib
print("\nvii. Plotting with Matplotlib:")
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.figure(figsize=(10, 5))

# Line plot
plt.subplot(1, 3, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")

# Bar plot
plt.subplot(1, 3, 2)
plt.bar(x, y)
plt.title("Bar Plot")

# Scatter plot
plt.subplot(1, 3, 3)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()