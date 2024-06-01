#Data Standardisation 
#The process  of Standardising the data to a common format and common range 
import numpy as np
import pandas as pd
import sklearn.datasets

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#loading the dataset
dataset = sklearn.datasets.load_breast_cancer()
df = pd.DataFrame(dataset.data,columns=dataset.feature_names)
df.head()

X=df
Y=dataset.target
print(X)
X.head()

#Splitting the data into train and test data 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

#Standardize the Data
#The standard deviation is a measure of the amount of variation or dispersion in a set of values.
# In the context of a dataset, it quantifies how much the individual data points differ from the mean (average) of the data.

print(dataset.data.std())
print(X_train)

#create a standard scaler instance
scaler = StandardScaler()
scaler.fit(X_train)
X_train_standardised = scaler.transform(X_train)
print(X_train_standardised)

X_test_Standardised = scaler.fit_transform(X_test)
print(X_test_Standardised.std())

