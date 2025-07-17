#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day 2 and 3
a=10
b=0
c=80
if a>b:
    if a>c:
        print("a")
    else:
        print("c")
elif b>a:
        if b>c:
            print("b")
        else:
            print("c")


# In[ ]:


#while loop
x=int(input("Enter a number"))
i=1
while i<=10:
    print(x,"x",i,"=",x*i)
print(10



# In[ ]:


#while loop
x=int(input("Enter a number"))
i=1
while i<=10:
    print(x,"x",i,"=",x*i)
    


# In[3]:


num=50
while num>=1:
    print(num)
    num=num-1


# In[6]:


num=int(input("Enter a number"))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")


# In[8]:


count=0
for i in range(1,101):
    if i%5==0:
        count=count+1
print(count)


# In[20]:


year=int(input("Enter a year"))
if year%2==0 or year%400==0 or year%200==0:
    print("Leap year")
else:
    print("Not a leap year")


# In[22]:


num=int(input("Enter a number"))
factorial=1
while num>0:
    factorial=factorial*num
    num=num-1
print(factorial)


# In[25]:


num=int(input("Enter a number"))
if num>0:
    print("Positive")
elif num<-1:
    print("Negative")
else:
    print("Zero")


# In[ ]:


num=int(input("Enter a number"))
if num>10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")


# In[30]:


for i in range(1,51):
    if i%3==0:
        continue
    else:
        print(i)


# In[33]:


string=str(input("Enter a string"))
for i in string:
    if i=="z":
        break
    else:
        print(i)


# In[36]:


num=int(input("Enter a number"))
count=0
digit=0
while(num!=0):
    digit=num%10
    if digit>0 or digit<-1 or digit==0:
        count=count+1
        num=num/10;
print(count)


# In[ ]:


num1=int(input("Enter number"))
num2=int(input("Enter number"))
num3=int(input("Enter number"))
num4=int(input("Enter number"))
num5=int(input("Enter number"))
avg=num1+num2+num3+num4+num5/5
print(avg)


# In[ ]:


c=str(input("Enter character"))
if c == 'a' or a == 'e' or a =='o' or a == 'i' or a == 'u':
    print("vowel")
else:
    print("not vowel")


# In[ ]:


i=50
while(i<101):
    if i%2!=0:
        odd=odd+1
        i=i+1
print(odd)


# In[ ]:


i=50
while(i<101):
    if i%2!=0:
        odd=odd+1
        i=i+1
print(odd)


# In[ ]:


i=50
while(i<101):
    if i%2!=0:
        odd=odd+1
        i=i+1
print(odd)


# In[ ]:


count=0
for i in range(1,11):
    num=int(input("Enter a number"))
    if num>=0:
        count=count+1;
print(count)


# In[ ]:




