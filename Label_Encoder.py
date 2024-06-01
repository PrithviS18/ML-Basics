#Label Encoding
#Converting the labels into numeric form

import pandas as pd
from sklearn.preprocessing import LabelEncoder

#loading the csv data into pandas dataframe
pd_dataframe = pd.read_csv('/content/breast_cancer_data.csv')
pd_dataframe.head()

#finding the count of different labels
pd_dataframe['diagnosis'].value_counts()
#create a LabelEncoder instance
label_encoder = LabelEncoder();

labels = label_encoder.fit_transform(pd_dataframe.diagnosis)

#Append this new label column to dataFrame
pd_dataframe['target'] = labels

