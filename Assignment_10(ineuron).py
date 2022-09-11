#!/usr/bin/env python
# coding: utf-8

# # Assignment_10(ineuron)
submitted by- Vishali R
# In[1]:


# 1. Write a Python program to find sum of elements in list?

a = list(map(int,input("Enter a list of integers:").split()))
print("The sum of elements in the given list is",sum(a))


# In[2]:


# 2. Write a Python program to Multiply all numbers in the list?

a = list(map(int,input("Enter a list of integers:").split()))
b = 1
for i in a:
   b *= i 
print("The multiplication of all numbers in the given list is:",b)


# In[3]:


# 3. Write a Python program to find smallest number in a list?

a = list(map(int,input("Enter a list of integers:").split()))
print("The smallest number in a list is:",min(a))


# In[5]:


# 4. Write a Python program to find largest number in a list?

a = list(map(int,input("Enter a list of integers:").split()))
print("The largest number in a list is:",max(a))


# In[8]:


# 5. Write a Python program to find second largest number in a list?

a = list(map(int,input("Enter a list of integers:").split()))
a.sort()
print("The second largest number in a list is:",a[-2])


# In[15]:


# 6. Write a Python program to find N largest elements from a list?

a = list(map(int,input("Enter a list of integers:").split()))
b = int(input("Enter the value of n:"))
a.sort(reverse = True)
print("The N largest elements in a list is:")
for i in range(b):
    print(a[i],end = " ")


# In[17]:


# 7. Write a Python program to print even numbers in a list?

a = list(map(int,input("Enter a list of integers:").split()))
b = [i for i in a if i%2==0]
print("The even numbers in a list is:")
print(*b)


# In[18]:


# 8. Write a Python program to print odd numbers in a List?

a = list(map(int,input("Enter a list of integers:").split()))
b = [i for i in a if i%2!=0]
print("The odd numbers in a list is:")
print(*b)


# In[15]:


# 9. Write a Python program to Remove empty List from List?

a = list(map(str,input("Enter a list:").split(",")))
for i in a:
    if type(i)==list and len(i)==0:
        a.pop(i)
print(*a)


# In[5]:


# 10. Write a Python program to Cloning or Copying a list?

a = list(map(int,input("Enter a list:").split(" ")))
b = a[:]
print("The cloned list is:",*b)


# In[7]:


# 11. Write a Python program to Count occurrences of an element in a list?

a = list(map(int,input("Enter a list:").split(" ")))
c = int(input("Enter the element to be counted:"))
print(c,"occured",a.count(c),"times")

