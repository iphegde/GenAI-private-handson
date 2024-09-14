import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset = sklearn.datasets.load_breast_cancer()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df.head()

# print(dataset)