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


# In[30]:


#directory
d={"apple":"red","orange":"orange","banana":"yellow","avacado":"brown"}
print(d.get("apple"))
print(d.keys())
print(d.values())
print(d.items())
d.update({"peach":"pink"})
print(d)
dic=d.copy()
print(dic)
print(d.pop("apple"))
print(d.popitem())
print(d.clear())


# In[52]:


#file handing
import os
file=open("myfile.txt","w")
file.writelines("Day 5 of learning python,i have learned about data types,list,set,while loop,for loop,if elif else statement,dictionaries.\n,i am studying file handing right now wish me luck")
file.close()
file=open("myfile.txt","r")
content=file.readline()
print(content)
content=file.readlines()
print(content)
file.close()
file=open("myfile.txt","r")
content2=file.read()
print(content2)
file.close()
os.remove("myfile.txt")


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


# In[56]:


#exception handing
try:
    x=int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Invalid Input:Please Enter a number.")


# In[60]:


try:
    a=int(input("Enter number"))
    b=int(input("Enter number"))
    result=a/b
    print("Result:",result)
except ValueError:
    print("Enter number")
except ZeroDivisionError:
    print("Cannor Divide by zero")


# In[59]:


try:
    num=int(input("Enter a number"))
except ValueError:
    print("That is not a number")
else:
    print("Square is:",num*num)


# In[72]:


def CheckAge(age):
    if age<18:
        raise ValueError("You must be at least 18 years old")
    return "Access Granted"
try:
    age=int(input("Enter a number:"))
    print(CheckAge(age))
except ValueError as e:
    print(e)


# In[77]:


#oops Concept
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print(f"name:{self.name},Age:{self.age}")
s1=Student("Diyank",23)
s1.show_details()

