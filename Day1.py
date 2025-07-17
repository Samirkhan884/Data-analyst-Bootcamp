#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Datatypes
a=5
print(type(a))
a=4.4
print(type(a))
a=True
print(type(a))
a=3
b=str(a)
print(type(b))


# In[6]:


#Arithmetic Operators
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=a+b
print(c)
c=a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c=a**b


# In[7]:


#Comparison Operators
a=10
b=15
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)


# In[15]:


#Question 1 
x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))
sum=x+y+z
print(sum)
avg=sum/3
print(avg)
print("is avg greater than 50")
print(avg>50)
print("is sum divisible by 5")
print(sum%5==0)


# In[9]:


#Logical Operators
a=10
b=26
print(a==b and a<b)
print(a==b or a<b)
print(not(a>b))


# In[11]:


#Membership Operator
a=[3,6,2,7]
for x in a:
    print(x)
a="java is easy to learn"
print("python" in a)
print("python" not in a)


# In[12]:


#Question 2
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
addition=num1+num2
print(addition)
multiplication=num1*num2
print(multiplication)
print("is number1 equal to number2")
print(num1==num2)
print("is num1 greater than num2")
print(num1>num2)
allowed=[10,20,30,40,50]
print("is num1 in allowed")
print(num1 in allowed)
print("is num2 in allowed")
print(num2 in allowed)


# In[14]:


#Identity Operator
a="python"
b="pyhton"
print(a is 6,b is not 6)

