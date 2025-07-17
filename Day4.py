#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day 4
#list
a=[7,'5',7.6]
print(type(a))
a.append(100)
a.insert(1,50)
a.extend([1,2])
a.pop()
a.remove(7.6)
# a.clear()
print(a.index(50))
print(a.count(7))
# a.sort() for ascending
# a.sort(-1) for decending '
#a.copy()
print(a.reverse())
print(a)


# In[40]:


num=123
digit=0
rev=0
for i in range(1,4):
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
print(rev)


# In[46]:


num=123
digit=0
sum=0
for i in range(1,4):
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)


# In[50]:


def factorial(n):
    if n==1 or n== 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


# In[55]:


def fibonacci(n):
    a=0
    b=1
    count=0
    while count<n:
        print(a,end=" ")
        temp=a+b
        a=b
        b=temp
        count+=1
fibonacci(5)


# In[71]:


oddsum=0
evensum=0
for i in range(1,6):
    if i%2!=0:
        oddsum=oddsum+i
    else:
        evensum=evensum+i
print(oddsum)
print(evensum)     


# In[4]:


for num in range(1,11):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[9]:


two=0
three=0
for i in range(1,11):
    two=two+2*i
    three=three+3*i
avg=(two+three)/20
print(avg)


# In[18]:


two=0
seven=0
for i in range(1,11):
    two=2*i
    seven=7*i
    avg=(two+seven)//2
    print("Avg of 2 and 7 tables =",avg)


# In[41]:


lst=[4,8,1,2]
lst.append(3)
lst.insert(1,5)
lst.extend([13,51])
lst.pop()
lst.remove(4)
lst.index(1)
lst.count(8)
print(lst)
lst.sort()
print(lst.sort())
lst.reverse()
b=[]
b=lst.copy()
print(lst)
print(b)
lst.clear()
print(lst)


# In[46]:


#slicing
num=[0,1,2,3,4,5,6,7,8,9,10]
print(num[0:4])
print(num[4:])
print(num[::-1])


# In[49]:


#list comprehension
[i**2 for i in [1,2,3]]


# In[51]:


[10*i+j for i in [1,2,3] for j in [5,7]]


# In[ ]:




