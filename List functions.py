#!/usr/bin/env python
# coding: utf-8

# In[10]:


#list questions
#question1
lst1=[]
for i in range(0,5):
    x=int(input("Enter number"))
    lst1.append(x)
print(lst1)


# In[2]:


#question2
lst2=[1,2,3]
lst3=[4,5,6]
lst2.extend(lst3)
print(lst2)


# In[3]:


#question3
l=[10,20,30,40]
l.insert(2,25)
print(l)


# In[4]:


#question4
l.remove(20)
print(l)


# In[5]:


#question5
print(l.pop())
print(l)


# In[6]:


#question6
lst4=[5,10,15,20,25]
print(lst4.index(15))


# In[7]:


#question7
lst5=[1,2,3,2,4,2]
print(lst5.count(2))


# In[8]:


#question8
lst6=[10,5,7,3]
lst6.sort(reverse=True)
print(lst6)
lst6.sort(reverse=False)
print(lst6)


# In[9]:


#question9
lst7=[1,2,3,4,5]
lst7.reverse()
print(lst7)


# In[ ]:




