import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = { 'Name': ['Subhranil','Abhishek'],
        'Age':[30,46],
        'State':['Jharkhand','Bihar']}

df = pd.DataFrame(data)
print(df)
print(df['Name'])
print(df.Age)
df['Salary']=[10,20]
print(df)