#Importing necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv('claims.csv')
data.info()
print(data.isnull().sum())
data=data.drop_duplicates()
data['claim_date']=pd.to_datetime(data['claim_date'], errors='coerce') #errors='coerce' does nothing but replaces empty columns of claim_date with NaN.

print(data.head())

#standardizing the data
scaler=StandardScaler()
data[['claim_amount']]=scaler.fit_transform(data[['claim_amount']])

data['year']=pd.DatetimeIndex(data['claim_date']).year
data['month']=pd.DatetimeIndex(data['claim_date']).month

data.to_csv('cleaned_claims.csv', index=False)