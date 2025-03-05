import pandas as pd

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
