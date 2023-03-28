#!/usr/bin/env python
# coding: utf-8

# # In Class Assignment #5: File IO, Recursion
# 
# ## Submit this assignment completed, in its own repository, as a GITHUB LINK. Cite your sources as always

# # PART 1. 
# Read in "numbers.txt" using the "open file" method we learned in class. Save the contents in a list variable called "L"
# 
# 

# In[13]:


filename = "C:/Users/nib/Documents/INFO 450/ICA5/numbers.txt"


# In[18]:


with open(filename) as file_object:
    a = file_object.read().split(',') #https://www.geeksforgeeks.org/file-objects-python/
    L = [int(i) for i in a] #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/

print(L)


# # PART 2. 
# 
# Write a Python function called "sum_recursive()" that takes a positive integer "n" as an input and 
# uses recursion to calculate the *sum of all integers* from 1 to "n". Your function should return the sum.
# 
# For example, if n is 5, your function should calculate and return the sum 1 + 2 + 3 + 4 + 5 = 15.
# 
# You can assume that the input n will always be a positive integer.
# 
# You should not use any built-in functions or methods that directly solve this problem (e.g. sum() or range()), 
# and you should use recursion to solve the problem.

# In[22]:


def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)


# In[23]:


sum_recursive(10)


# ## PART 3.
# 
# Write a Python function called "looping()" that takes a list of integers, runs each integer through "sum_recursive()", and returns the list of recursively summed integers.
# 
# ie. if your list is [2, 5, 3], your function output should be [3, 15, 6]

# In[24]:


def looping(integers):
    list = []
    for n in integers:
        list.append(sum_recursive(n))
    return list


# In[25]:


looping([2, 5, 3])


# ## PART 4. 
# You probably saw this coming by now..
# 
# Please run the contents of the "numbers.txt" file (you completed in PART 1) through your "looping()" function

# In[19]:


looping(L)

