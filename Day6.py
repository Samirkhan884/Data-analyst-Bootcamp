#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Day 6
#sqlite3
import sqlite3


# In[17]:


import sqlite3
conn=sqlite3.connect('students.db')
#creating a cursor object
cursor=conn.cursor()


# In[18]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()
print("Table created successfully.")


# In[19]:


def insert_student(name,age,grade):
    cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)", (name,age,grade))
    conn.commit()
    print("Student inserted successfully.")
insert_student('Vikas',19,'O')
insert_student('Aman',23,'C')
insert_student('Dev',22,'A')


# In[20]:


def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
fetch_students()


# In[21]:


def update_student(student_id,new_name,new_age,new_grade):
    cursor.execute("UPDATE students SET name=?,age=?,grade=? WHERE id=?",(new_name,new_age,new_grade,student_id))
    conn.commit()
    print("Student Updated successfully.")
update_student(4,'vikas',19,'O')


# In[22]:


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?",(student_id,))
    conn.commit()
    print("Student Deleted successfully.")
delete_student(2)


# In[23]:


conn.close()
print("Connection Close successfully.")


# In[27]:


#numpy


# In[3]:


import numpy as np


# In[15]:


a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
print(a)
print(b)


# In[12]:


arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)


# In[20]:


a=np.array([1,2,3,4,5,6])
print(a.reshape(2,3))


# In[22]:


arr=np.array([10,20,30,40,50])
print(arr[1])
print(arr[1:4:1])


# In[32]:


print(np.zeros((2,3)))
print(np.ones((3,3)))
print(np.eye(3,3))
print(np.full(3,3))
print(np.arange(1,10,2))
print(np.linspace(1,5,4))


# In[8]:


a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(np.add(a,b))
print(np.multiply(a,b))
print(np.sqrt(a))


# In[13]:


arr=np.array([[1,2,3],[4,5,6]])
print(np.sum(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.argmax(arr))


# In[16]:


arr=np.array([4,1,5,6])
print(np.sort(arr))
print(np.unique(arr))


# In[4]:


arr=np.array([[1,2],[3,4]])
print(arr)
print(arr.flatten())


# In[38]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.T)

