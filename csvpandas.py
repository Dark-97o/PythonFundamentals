import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print("DataFrame created using pandas:")
print(df)
df = pd.read_csv(r"C:\Users\DELL\Downloads\emotion_dataset.csv")
print("DataFrame loaded from CSV file:")
print(df)

from sklearn.datasets import load_iris
iris = load_iris()
print("Description of the Iris dataset:")
print(iris.DESCR)
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print("DataFrame created from the Iris dataset:")
print(df)

#LB 6.2
list = [2, 4, 4, 4, 5, 5, 7, 9]
print(np.average(list))
print(np.var(list))
print(np.std(list))
