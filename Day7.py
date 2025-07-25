#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 7


# In[2]:


#pandas


# In[2]:


import pandas as pd


# In[13]:


#from directory
data={'Name':['Divyank','Riya','Aryan'],'Age':[21,20,22],'marks':[88,92,79]}
df=pd.DataFrame(data)
print(df)


# In[13]:


df1=pd.read_csv('input.csv')
print(df1)
df2=pd.DataFrame(data={'Name':['nmplol','arther','hasanabi'],'Age':[21,20,22],'marks':[88,92,79]})
df2.to_csv('output.csv',index=False)
print(df2)
df_excel1=pd.DataFrame({'Name':['samir','vikas','aman'],'Age':[99,98,79]})
df_excel1.to_excel('input.xlsx',index=False)
#df_excel2=pd.DataFrame()
df_excel2=pd.read_excel('input.xlsx',engine='openpyxl')
print(df_excel2)


# In[31]:


print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())


# In[43]:


print(df['Name'])
print(df[['Name','Marks']])
print(df.loc[0])
print(df.iloc[1])


# In[55]:


data={'Name':['Divyank','Riya','Aryan'],'Age':[21,20,22],'Marks':[88,92,79]}
df=pd.DataFrame(data)
print(df[df['Marks']>85])
print(df[(df['Marks']>85) & (df['Age']<22)])


# In[56]:


df['Grade']=['A','B','C']
df['Marks']=df['Marks']+5
print(df)


# In[57]:


df.drop('Grade',axis=1,inplace=True)
print(df)
df.drop(1,axis=0,inplace=True)
print(df)


# In[59]:


print(df.sort_values(by='Marks',ascending=False))


# In[66]:


df=pd.DataFrame({'Name':['A','B',None],'Marks':[80,None,75]})
print(df)
df.fillna({'Name':'unknown','Marks':0},inplace=True)
print(df)
df.dropna(inplace=True)
#print(df)


# In[22]:


df=pd.DataFrame({'Department':['IT','IT','HR','HR'],'Salary':[50000,60000,45000,47000]})
print(df.groupby('Department')['Salary'].mean())


# In[21]:


df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['A', 'B']})
df2 = pd.DataFrame({'ID': [1, 2], 'Marks': [80, 90]})
df3=pd.merge(df1,df2,on='ID')
print(df3)


# In[67]:


import matplotlib.pyplot as plt


# In[5]:


x=[1,2,3,4]
y=[10,20,30,40]
#plt.plot(x,y)
#plt.bar(x,y)
plt.barh(x,y)
plt.title("basic line plot")
plt.xlabel("x-axis")
plt.ylabel("y=axis")
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2  


img = cv2.imread("img.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  


plt.title("Original image")
plt.imshow(img_rgb)
plt.axis('off')
plt.show()

pixels = img_rgb.reshape(-1, 3)
df = pd.DataFrame(pixels, columns=['R', 'G', 'B'])
print("Original pixels:")
print(df.head())


df['R'] = 0
modified_pixels = df.to_numpy().astype(np.uint8)
modified_img = modified_pixels.reshape(img_rgb.shape)


plt.title("Modified image (no red)")
plt.imshow(modified_img)
plt.axis('off')
plt.show()


# In[ ]:




