import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset to a pandas dataFrame
dataset = pd.read_csv('/content/Placement_Dataset.csv')
dataset.head()

dataset.isnull().sum() #to find the number of missing values in each column
#filling missing values with the median values
dataset['salary'].fillna(dataset['salary'].median(),inplace=True)

#filling missing values wih the mean values
dataset['salary'].fillna(dataset['salary'].mean(),inplace=True)

#filling missing values with the mode values
dataset['salary'].fillna(dataset['salary'].mode(),inplace=True)
