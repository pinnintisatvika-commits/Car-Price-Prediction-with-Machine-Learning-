import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics
car_dataset = pd.read_csv('/content/car data.csv')
car_dataset = pd.get_dummies(car_dataset, drop_first=True)
print(df.shape)

print(df.info())

print(df.describe())

print(df.isnull().sum())