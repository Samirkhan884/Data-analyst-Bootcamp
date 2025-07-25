#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv('Data2.csv')
print("top 5 rows")
print(df.head())
print("Info")
print(df.info())
print("Describe")
print(df.describe())
df = df.drop_duplicates()
print("Null values")
print(df.isnull().sum())
df = df.replace('', np.nan)
df=df.dropna()
print("Null values after using dropna")
print(df.isnull().sum())
x=[]
x = df[df["Released_Year"] > 2015]["Star"]
y=[]
y=df[df["Released_Year"] > 2015]["IMDB_Rating"]
plt.plot(x,y)
plt.show()


# In[ ]:




