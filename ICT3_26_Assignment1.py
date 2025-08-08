#!/usr/bin/env python
# coding: utf-8

# In[1]:


# (Q1). Given a two integer numbers return their product and  if the product is greater
# than 1000, then return their sum


def Product_of_sum(a,b):
    product=a*b
    if product>1000:
        return a+b
    else:
        return product

a=int(input("Enter Frist No "))
b=int(input("enter Second no "))

result = Product_of_sum(a,b)
print("result: ",result)


# In[6]:


# Q2. Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous numbe

def sum_current_previous():
    a=int(input("Input a number"))
    previous = 0
    for current in range (a):
        print(f"Current: {current}, Previous: {previous}, Sum: {current + previous}")
        previous = current

sum_current_previous()


# In[7]:


# 3. Given a string, display only those characters which are present at an even index number.

def even_index_chars(s):
    return s[0::2]

print(even_index_chars("HELLO_WORLD"))


# In[12]:


# 4. Given a list of numbers, return True if first and last number of a list is same

def first_last_same(lst):
    if len(lst) == 0:
        return False
    return lst[0] == lst[-1]


print(first_last_same([10, 20, 30, 10]))  
print(first_last_same([5, 6, 7,8,10,6])) 


# In[16]:


# 5. Given a two list. Create a third list by picking an odd-index element from the first
# list and even index elements from second.


def merge_odd_even(list1, list2):
    result = []
 
    result.extend([list1[i] for i in range(1, len(list1), 2)])
  
    result.extend([list2[i] for i in range(0, len(list2), 2)])
    return result


list1 = [10, 11, 12, 13, 14, 15]
list2 = [20, 21, 22, 23, 24, 25]
print(merge_odd_even(list1, list2))


# In[ ]:


# 6. Given an input list removes the element at index 4 and add it to the 2nd position
# and also, at the end of the list

def modify_list(lst):
    if len(lst) > 4:
        element = lst.pop(4)
        lst.insert(1, element)
        lst.append(element)
    else:
        print("Enter the at list 5 element.")
    return lst

user_input = input("Insert list element sepreter by comm: ")
input_list = [x.strip() for x in user_input.split(",")]

result = modify_list(input_list)
print("Modified list:", result)


# In[20]:



# 7. Given a list slice it into a 3 equal chunks and reverse each list

def slice_and_reverse(lst):
    n = len(lst)
    chunk_size = n // 3
    chunks = [lst[i*chunk_size:(i+1)*chunk_size] for i in range(3)]
    reversed_chunks = [chunk[::-1] for chunk in chunks]
    return reversed_chunks

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(slice_and_reverse(my_list))


# In[25]:


# 8. Given a list iterate it and count the occurrence of each element and create a
# dictionary to show the count of each element

def count_occurrences(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_occurrences(my_list))


# In[26]:


# 9. Add a list of elements to a given set: {‘yellow’,’orange’} List:[blue,black]

my_set = {'yellow', 'orange'}
new_elements = ['blue', 'black']

my_set.update(new_elements)

print(my_set)


# In[28]:



# 10. Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


# In[29]:


# 11. calculate the sum of all number between 1 and given number
def sum_between_1_and_n(n):
    return sum(range(1, n + 1))
print(sum_between_1_and_n(10))


# In[32]:


# 12. Given a list iterate it and display numbers which are divisible by 5 and if you find
# number greater than 150 stop the loop iteration

def display_divisible_by_5(lst):
    for num in lst:
        if num > 150:
            break
        if num % 5 == 0:
            print(num)
            
numbers = [10, 25, 33, 50, 120, 155, 5, 200]
display_divisible_by_5(numbers)


# In[ ]:





# In[ ]:




