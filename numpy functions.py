#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy assignment


# In[2]:


import numpy as np


# In[4]:


#question1
arr=np.arange(1,11)
print(arr)


# In[9]:


#question2
arr1=np.zeros((10))
arr1[4]=1
print(arr1)


# In[12]:


#question3
arr2=np.ones((10))
print(arr2)


# In[14]:


#question4
arr3=np.random.rand(0,1)
print(arr3)


# In[17]:


#question5
arr4=np.linspace(0,1,20)
print(arr4)


# In[22]:


#question6
arr5=np.eye((3))
print(arr5)


# In[24]:


#question7
arr6=np.arange(16).reshape(4,4)
print(arr7)


# In[27]:


#question8
arr7=np.random.rand(5,5)
print(arr8)


# In[56]:


#question9
arr8=np.array([1,2,3,4,5])
rev=arr9[::-1]
print(rev)


# In[37]:


#quesiton10
arr9=np.array([[2,5,1],[1,4,7]])
print(arr10.flatten())


# In[55]:


#question11
arr10=([1,2,3,4,5,6,7,8,9,10])
arr11=[]
for i in arr10:
    if i%2==0:
        arr11.append(i)
even=np.array(arr11)
print(even)

