import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Raj', 'Rahul', 'Riya', 'Rohan'],
        'Age': [46, 24, 23, 22],
        'States': ['Punjab', 'Haryana', 'Delhi', 'UP']}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nAccessing Columns:")
print(df['Name'])
print(df.Age)  
print("\nAccessing Rows:")
print(df.loc[0])  
print(df.iloc[0])  
print("\nFiltering Data:")
print(df[df['Age'] > 30]) 
df['Salary'] = [150000, 120000, 100000, 80000]
print("\nDataFrame with New Column:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

def line_plot():
        import matplotlib.pyplot as plt
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Line Plot')
        plt.show()

def scatter_plot():
        import matplotlib.pyplot as plt
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Scatter Plot')
        plt.show()

def bar_plot():
        import matplotlib.pyplot as plt
        categories = ['A', 'B', 'C', 'D']
        values = [20, 30, 25, 35]
        plt.bar(categories, values, color='green')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Bar Plot')
        plt.show()

def histogram():
        import matplotlib.pyplot as plt
        import numpy as np
        np.random.seed(0)
        data = np.random.randn(1000)
        plt.hist(data, bins=30, color='blue', edgecolor='black')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()

ch = int(input("Enter your choice:\n1 for Line Plot\n 2 for Scatter Plot\n 3 for Bar Plot\n 4 for Histogram: "))
if ch == 1:
        line_plot()
elif ch == 2:
        scatter_plot()
elif ch == 3:
        bar_plot()
elif ch == 4:
        histogram()
else:
        print("Invalid Choice")