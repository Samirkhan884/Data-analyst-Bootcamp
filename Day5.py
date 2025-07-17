#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Day 5


# In[9]:


#tuple
tuple1=tuple([1,2,3,4,5,5,5])
print(tuple1)
print(tuple1.count(5))
print(tuple1.index(1))


# In[ ]:


#string method is homework


# In[46]:


#set
set0=set()
set1=set([1,2,3,])
print(type(set1))
print(type(set0))
set2=set([2,3,4,5])
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
#print(set2.symeticdifference(set2))
print(set1.issubset(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))


# In[51]:


#dictionary
file=open("myfile.txt","w")
content=file.write("this is test 2")
file.close()
file=open("myfile.txt","r")
content=file.read()
print(content)
file.close()


# In[1]:


def countGender(male,female):
    for i in range(3):
        for j in range(2):
            if family[i][j]=='m':
                male=male+1
            else:
                female=female+1
    if male>female:
        print("male is dominant")
    elif female>male:
        print("female is dominant")
    else:
        print(" both are balanced")
fam1=[]
fam2=[]
fam3=[]
family=[fam1,fam2,fam3]
for i in range(3):
    for j in range(2):
        x=str(input("Enter M for Male and f for Female"))
        family[i].append(x)
male=0
female=0
countGender(male,female)

