#importing the dependencies
import numpy as np
import pandas as pd

#loading the dataset to pandas dataframe
credit_card_data = pd.read_csv('/content/credit_data.csv')
credit_card_data.head()

#Checking the count of different values in the 'Class' column
credit_card_data.Class.value_counts()

#It is a highly imbalanced dataset as count of 0 is almost 99% 
#0 --> legal transactions 
#1 --> fraud transactions

#Separating the two values
legit=credit_card_data[credit_card_data.Class==0]
fraud=credit_card_data[credit_card_data.Class==1]
print(legit.shape)

#Under Sampling
#Building a sample dataset containing similar distribution of legit and faundulent transactions
#The number of fraudulent Transactions is = 81, so we create a sample of 81 data from legit transactions

#creating legit_sample that contains 81 random values from the legit dataset
legit_sample = legit.sample(n=81)
print(legit_sample.shape)

new_dataset = pd.concat([legit_sample,fraud],axis=0,ignore_index=True)


new_dataset.Class.value_counts()
