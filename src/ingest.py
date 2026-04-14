import pandas as pd
from sklearn.datasets import load_iris
import os

os.makedirs('data', exist_ok=True)
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.to_csv('data/iris.csv', index=False)
print("Data ingested successfully!")
