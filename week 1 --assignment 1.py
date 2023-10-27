#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q-1 create one variable containing following type of data:
#(1)string
s = 'mohd'
type(s)


# In[5]:


#(2)list
l = [1,2,3,4,5]
type(l)


# In[7]:


#(3)float
a = 344.56
type(a)


# In[8]:


#(4)tuple 
t = ('arif','mohd',2,4,5)
type(t)


# In[9]:


#Q-2.Given are some following variables containing data:
#(1)
var1 = ''
type(var1)


# In[11]:


#(2)
var2 = '[DS,ML,Python]'
type(var2)


# In[12]:


#(3) 
var3 = ['DS','ML','Python']
type(var3)


# In[13]:


#(4)
var4 = 1
type(var4)


# In[14]:


#Q-3.Explain the use of the following operators using an example:
#(1)/
a = 10 
b = 5
print(a/b)


# In[15]:


#(2)%
a = 9
b = 2
print(a%b)


# In[16]:


#(3)//
a = 9
b = 2
print(a//b)


# In[17]:


#(4)**
a = 2
b = 3
print(a**b)


# In[18]:


#Q-4.Create a list of length 10 of your choice containing multiple types of data.
#Using for loop print the element and its data type.

l = ['arif',43,45.23,True,4+3j,False,'mohd',2,3,4]
for i in l:
    print(type(i))
    


# In[35]:


#Q-5.Using a while loop,verify if the number A is purely divisible by number B 
#and if so then how many times it can be divisible.

a = 81
    
count = 0

b = 3

while a > 0:
    if a % b == 0:
        count = count + 1
    a = a / b 
if a == 1:
    count = count + 1
    
print(count)


# In[36]:


#Q-6.Create a list containing 25 int type data.
#Using for loop and if-else condition print if the element is divisible by 3 or not.
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25]
for n in list:
    if n % 3 == 0:
        print("n is divisible by 3")
    else:
        print("n is not divisible by 3")


# In[39]:


#Q-7.What do you understand about mutable and immutable data types? 
#Give examples for both show this property.

#MUTABLE:
       #Mutable data types,on the other hand,can be modified after creation.
        #This means that you can change their contents in-place without creating a new object.
list = [1,2,3]
list.append(4)
list[0] = 100
print(list)


# In[45]:


#Immutable:
          #Immutable data types are generally safer in a multi-threaded environment
           #because they cannot be changed after creation.
        
        
s = "Arif"
s[1] = 'd'
        


# In[ ]:




