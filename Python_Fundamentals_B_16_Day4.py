#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Introduction to list datatype

students=['abhijeet','raj','karan','abhishek','rahul']

print(students)


# In[2]:


type(students)


# In[4]:


#indexing

print(students[0])


# In[5]:


students[0]='ajay' #reassigning ajay at 0 index

print(students)


# In[7]:


students.append('abhijeet') #adding new item to the list and by default with append method item will be added to the last index

print(students)


# In[16]:


#inserting a new item at a specific index using insert method

students.insert(1,'chetan')

print(students)


# In[12]:


# Removing item from the list using pop method

# By default pop method will remove the last index item of the list

students.pop()



# In[13]:


print(students)


# In[18]:


# But we can pass index as an argument and it will remove that index item

students.pop(2)


# In[19]:


print(students)


# In[21]:


# Removing item at specific index in the list using delete function

del students[0]


# In[24]:


print(students)


# In[26]:


# using f string and list in same code

print(f"All the best, {students[0].title()}!!")


# In[28]:


# Inbuilt list menthods

students.clear() # to the clear the elemets of the list


# In[29]:


print(students)


# In[30]:


students=['abhijeet','raj','karan','abhishek','rahul']


# In[31]:


print(students)


# In[34]:


students1=students.copy() # to copy from one list to another


# In[35]:


print(students1)


# In[39]:


students.append('abhijeet')


# In[40]:


print(students)


# In[41]:


CountOfElements=students.count('abhijeet') # Count method is used to find how many times one element appreas in a list


# In[42]:


print(CountOfElements) 


# In[46]:


# Extend method

List1=[1,2,3]
List2=[4,5,6]

List1.extend(List2) # to extend elements of another list to current list at the end

print(List1)
print(List2)


# In[48]:


# Remove Method

print(students)

students.remove('raj') # to remove specific element from the list


# In[49]:


print(students)


# In[51]:


# Reverse Method

students.reverse() # it will the revers the order of the elements in the list


# In[52]:


print(students)


# In[54]:


#Sort Method

students.sort() # it will sort the list in the alphabatical order

print(students)


# In[ ]:




