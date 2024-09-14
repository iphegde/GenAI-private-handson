# importing the pandas library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





# importing the boston house price data
# from sklearn.datasets import fetch_california_housing
# housing = fetch_california_housing()
#type(housing)
# print(housing)


# pandas DataFrame
# housing_df = pd.DataFrame(housing.data , columns = housing.feature_names)

# print(housing_df)

# housing_df.head()
# print(housing_df.shape)

#housing_df.to_csv("housing_data.csv")

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)

# print(x)
# print(y)
# print(z)


#Sine Wave
# plt.plot(x,z)
# plt.show()

plt.plot(x,z)
plt.xlabel('angle')
plt.ylabel('sine')
plt.title('Wave')
plt.show()