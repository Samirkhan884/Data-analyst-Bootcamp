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


# In[102]:


lst1=[]
for i in range(0,5):
    x=int(input("Enter number"))
    lst1.append(x)
print(lst1)
lst2=[1,2,3]
lst3=[4,5,6]
lst2.extend(lst3)
print(lst2)
l=[10,20,30,40]
l.insert(2,25)
print(l)
l.remove(20)
print(l)
print(l.pop())
print(l)
lst4=[5,10,15,20,25]
print(lst4.index(15))
lst5=[1,2,3,2,4,2]
print(lst5.count(2))
lst6=[10,5,7,3]
lst6.sort(reverse=True)
print(lst6)
lst6.sort(reverse=False)
print(lst6)
lst7=[1,2,3,4,5]
lst7.reverse()
print(lst7)


# In[119]:


def countGender(male,female):
    for i in range(3):
        for j in range(2):
            if family[i][j]=='m':
                male=male+1
            else:
                female=female+1
    if male>female:
        print("male")
    elif female>male:
        print("female")
    else:
        print("balanced")
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


# In[29]:


class Bank:
    def __init__(self,cname,accountid,balance):
        self.cname=cname
        self.accountid=accountid
        self.balance=balance
    def deposit(self,damount):
        balance=balance+amount
        print("balance:",balance)
    def withdraw(self,wamount):
        if wamount>=500:
            balance=balance-wamount
        else:
            print("Enter a valid amount(above 500)")
    def showBalance(self):
        print("account_id :",accountid)
        print("balance :",balance)
c1=Bank("samir","BGN",5000)
c1.deposit(1000)
c1.withdraw(1000)
c1.showBalance()


# In[ ]:




