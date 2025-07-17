#!/usr/bin/env python
# coding: utf-8

# In[2]:


#while loop
x=int(input("Enter a number"))
i=1
while i<=10:
    print(x,"x",i,"=",x*i)
    i+=1


# In[10]:


x="samir1"
i=6
while False:
    y=str(input("Enter password"))
    if x==y:
        print("welcome samir khan") 
        break
    elif i==4:
        print("Are you sure U know the Password!")
        i=i-1
    else:
        print("Attempt Left",i,"\Try Again")
    i=i-1


# In[1]:


#for loop
a=[2,5,6,8]
for i in a:
    if i==6:
        print(12)
        continue
    print(i)


# In[15]:


for i in range(11):
    if i%2==0:
        print(i," is Even")
    else:
        print(i," is odd")


# In[26]:


num=int(input("Enter a number:"))
if num%3==0 and num%7==0:
    print("Num is divisible by both 3 and 7")
else:
    print("Num is not divisible by both 3 and 7")


# In[28]:


for i in range(1,101):
    if i%2==0:
        print(i)


# In[31]:


num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2:
    if num1>num3:
        print("num1 is the greatest")
    else:
        print("num3 is the greatest")
elif num2>num1:
    if num2>num3:
        print("num2 is the greatest")
    else:
        print("num3 is the greatest")


# In[ ]:


num=50
while num>=1:
    print(num)


# In[ ]:




