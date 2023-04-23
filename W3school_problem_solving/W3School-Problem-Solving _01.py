#!/usr/bin/env python
# coding: utf-8

# # W3School Python Problem Solving: List, Set, Tuples, Dictionary, List Advanced
#     
# In this task, I have completed and solved several basic level python coding problem with the help of different methods, control flow, user-defined functions, and object oriented mechanism as well as built-in methods in Python. The exercises in this task cover a range of basic Python programming concepts, including sets, lists, dictionaries, and tuples. Each section of the exercise set provides a list of problems to solve, along with sample input and output to help guide you as you write your code.
# 
# In the Lists section, it discussed learn how to work with lists in Python, including how to create lists, add and remove elements from lists, and perform operations like sorting and reversing lists.
# 
# In the Sets section, it discussed how to work with sets in Python, including how to create sets, add and remove elements from sets, and perform operations like union, intersection, and difference on sets.
# 
# In the Tuples section, it discussed how to work with tuples in Python, including how to create tuples, access and modify tuple elements, and perform operations like unpacking and slicing tuples.
# 
# In the Dictionaries section, it discussed how to work with dictionaries in Python, including how to create dictionaries, add and remove key-value pairs from dictionaries, and perform operations like iterating over keys and values in dictionaries.
# 
# All the problems are situated in the W3School website. I have asserted all the questionnaires regarding to the python problem solving with reference materials below:
# 
# 1. https://www.w3resource.com/python-exercises/sets/
# 2. https://www.w3resource.com/python-exercises/list/
# 3. https://www.w3resource.com/python-exercises/dictionary/
# 4. https://www.w3resource.com/python-exercises/tuple/
# 5. https://www.w3resource.com/python-exercises/list-advanced/index.php

# # **** Example 1: Lists

# ## 1. Write a Python program to sum all the items in a list.

# In[2]:


def sum_list(number):
    total = 0
    for num in number:
        total += num
    return total

number = [23,34,45,65,67,89,76,43,22,12]
print("Sum of all Items: ", sum_list(number))

# Alternative version

number = [23,34,45,65,67,89,76,43,22,12]
total = 0

for i, num in enumerate(number): # Iterating with using indexing position using enumerate
    total += num
    print(f"\nThe {i+1}th number is {num}. Total is {total}")
    
print(total)

# Another One: Listing the every ith number sum value into a list

running_totals = []

total = 0
for num in number:
    total += num
    running_totals.append(total)
    
    
print(running_totals)


# ## 2. Write a Python program to multiply all the items in a list.

# In[4]:


def mul_list(number):
    total = 1
    for num in number:
        total *= num
    return total

print("Mulipilcation of list elements together: ", mul_list(number))


# ## 3. Write a Python program to get the largest number from a list

# In[5]:


def get_largest(number):
    largest = number[0]
    for num in number:
        if num > largest:
            largest = num
    return largest

print("Largest Number Given in a list: ", get_largest(number))  # output: 87


# ## 4. Write a Python program to get the smallest number from a list.

# In[6]:


def get_smallest(number):
    smallest = number[0]
    for num in number:
        if num < smallest:
            smallest = num
    return smallest
print("Smallest number of a given list among the elements: ", get_smallest(number))


# ## 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. 

# In[11]:


string_list = ['abc', 'xyz', 'aba', '1221']

count = 0   # define a variable 'count' to keep track of the number of strings 

for string in string_list:
    if len(string) >= 2 and string[0] == string[-1]: # if length greater than or equal 2 and first and last characters are the same
        count += 1
print("Number of Strings Satisfying the condition: ", count)

##########################

def name_words(words):
    strcount = 0
    strlist = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            strcount += 1
            strlist.append(word)
    return strcount, strlist

words = ["rehman", "lahul", "oragoto", "1221", "Mohua"]
count, strlist = name_words(words)

print("Number of Strings Satisfying the condition: ", count)
print("Strings Satisfying the condition: ", strlist)


# In[94]:


# Another version

string_list = ['abc', 'xyz', 'aba', '1221']

count = 0
lists = []
for string in string_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
        lists.append(string)
print(lists)

print("Number of Strings Satisfying the condition: ", count)
print("Number of Strings Satisfying the condition: ", string[1]) # Last element of 1221 with second index


# ## 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# In[95]:


tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(tuples, key=lambda x: x[-1])
print("sorted List: ", sorted_list)


# ## 7. Write a Python program to remove duplicates from a list.

# In[25]:


dup = [23,22,34,23,45,23,22,43,21,43,22]

dup_items = set()
uniq_items = []
for x in dup:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
print(uniq_items)

# Alternative Version

output = list(set(dup))
print("List after removing duplicates: ", output)

#########################################################

# For Character strings

food = ["apple", "banana", "orange", "apple", "grape", "banana"]

dup_items = set()
uniq_items = []
for x in food:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
print(uniq_items)

# Alternative Version

output = list(set(food))
print("List after removing duplicates: ", output)


# ## 8. Write a Python program to check if a list is empty or not.

# In[15]:


a = []
c = [21,21,31,41]

def find_empty(a):
    
    if not a:
        print("With an Empty List")
    else:
        print("EveryThing is Here")
             
b = find_empty(a)
b1 = find_empty(c)


# ## 9. Write a Python Program to Clone or Copy a List ?

# In[26]:


original_list = [1,2,3,4,5,6,7,8]
clone = original_list[:]

print("Original List: ", clone)
print("")


# ## 10. Write a Python program to find the list of words that are longer than n from a given list of words.

# In[17]:


def find_long_word(word_list, n):
    long_words = []
    for word in word_list:
        if len(word) > n:
            long_words.append(word)
    return long_words

word_list = ['batman', 'superman', 'spiderman', 'ironman', 'captain america', 'deadpool', 'antman']
n = 6

long_words = find_long_word(word_list, n)
print(f"Words with longer than {n} characters: {long_words}")


# ## 11. Write a Python function that takes two lists and returns True if they have at least one common member. 

# In[18]:


# Define fuction

def have_common_member(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False


list1 = [11, 22, 33, 44, 55,66]
list2 = [66, 77, 88, 99, 100, 111]

print(f"Do {list1} and {list2} have a common member? {have_common_member(list1, list2)}")


# ## 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# In[92]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

my_list = my_list[1:4] + my_list[6:]
print(my_list)


# ## 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# In[20]:


# Generate a 3x4x6 3D array of '*'

array_3D = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        for k in range(6):
            print(array_3D[i][j][k], end='')
        print()
    print()

    
# Another Version
array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# Print the 3D array
for row in array_3d:
    for sub_row in row:
        print(' '.join(sub_row))
    print()


# ## 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# In[21]:


def remove_even(list1):
  return [x for x in list1 if x % 2 != 0]

list1 = [1,2,3,4,5,6,7,8,9,10]
odd_list = remove_even(list1)
odd_list


# ## 15. Write a Python program to shuffle and print a specified list.

# In[22]:


import random

list1 = [1,2,3,4,5,6,7,8,9,10]

while True:
  user = input("Do You wann Shuffle The List Now?:(Y/N): ")
  if user == 'y':
    random.shuffle(list1)
    print(list1)
  elif user == 'n':
    print("Exiting the Operation...")
    break
  else:
    print("Invalid Input. Please Enter 'Y' or 'N'")

### Alternative Version

def shuffle_list(list2):
  random.shuffle(list2)
  return list2

list2 = [1,2,3,4,5,6,7,8,9,10]

shuffle_output = shuffle_list(list2)
print(f"A Single shuffle: {shuffle_output}")


# ## 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# In[17]:


""" is_square function computes the square of the floor of the square root of n, which is the largest perfect square less than or equal to n.
n**0.5 computes the square root of n. int((n**0.5)**2) == n checks whether the largest perfect square less than or equal to n is equal to n.
""" 
def is_square(n):
  return int(n**0.5)**2 == n   # Return True if n is a square number, otherwise it is False

# Generaing a list of square numbers between 1 and 30 both including
squares = [i for i in range(1,31) if is_square(i)] 

# Print the first and last 5 elements of the list
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])


# ## 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square numbers between 1 and 30 (both included).

# In[18]:


def is_square(n):
  return int(n**0.5)**2 == n   # Return True if n is a square number, otherwise it is False

# Generaing a list of square numbers between 1 and 30 both including
squares = [i for i in range(1,31) if is_square(i)] 

# Print the first and last 5 elements of the list
print("Elements Excepts First 5 elements:", squares[5:])

# Alternative Version:

squares = []
for i in range(1,31):
  if is_square(i):
    squares.append(i)

if len(squares) > 5:
  print("Elements Except First 5 Value")
  for i in range(5, len(squares)):
    print(squares[i])
else:
  print("The are less than 5 square numbers in the list.")


# ## 18. Write a Python program to generate all permutations of a list in Python.

# In[19]:


from itertools import permutations

list1 = [4,5,6,7]
permutation = permutations(list1)

for perms in permutation:
  print(perms)

# Another Alternative Method

def get_permutation(list1):

  if len(list1) == 0:
    return [[]] # return a list of all permutations of the input list
  else:
    result = []
    for i in range(len(list1)):
      """
      lst[:i] returns a list of all the elements of lst up to (but not including) index i,
      and lst[i+1:] returns a list of all the elements of lst after (but not including) index i.

      """    
      # using the loop variable i to represent the index of the current element.
      rest = list1[:i] + list1[i+1:]   # For each element of lst, the function creates a new list rest that contains all the elements of lst except the current one.
      for perm in get_permutation(rest):
        result.append([list1[i]] + perm)
    return result

list1 = [5,6,7,8]
perms = get_permutation(list1)

for perm in perms:
  print(perm)


# ## 19. Write a Python program to calculate the difference between the two lists.

# In[20]:


def difference(list1, list2):

  result = []
  for x in list1:
    if x not in list2:
      result.append(x)
  return result

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
diff = difference(list1, list2)
print(diff)

# Alternative Method
def difference(lst1, lst2):
    """
    Returns a list containing the elements that are in lst1 but not in lst2.
    """
    return list(set(lst1) - set(lst2))

list1 = [67,54,32,21,56,78,97,54]
list2 = [32,34,54,45,56,97,67]
diff = difference(list1, list2)
print(diff)


# ## 20. Write a Python program to access the index of a list.

# In[21]:


lst = ['apple', 'banana', 'cherry', 'durian']
for index, item in enumerate(lst):
    print(index, item)

# Alternative 

lst = ['apple', 'banana', 'cherry', 'durian']
for i in range(len(lst)):
    print(i, lst[i])



# ## 21. Write a Python program to convert a list of characters into a string. Go to the editor
# 

# In[103]:


char_list = ['S', 'a', 'k', 'i', 'b']

char_str = ''.join(char_list)
print(char_str)


# ## 22. Write a Python program to find the index of an item in a specified list. Go to the editor
# 

# In[108]:


def find_index(list1, item):

    """
    Finds the index of an item in a list.

    Args:
        lst: A list of items.
        item: The item to find the index of.

    Returns:
        The index of the item in the list, or -1 if the item is not in the list.
    """
    
    try:
        index = list1.index(item)
        return index
    except ValueError:
        return -1

my_list = ['apple', 'banana', 'orange', 'pear']
index = find_index(my_list, 'orange')
print(index)  

######## Alternative Method

def find_index(list1, item):
    for i in range(len(list1)):
        if list1[i] == item:
            return i
        
    return -1

my_list = ['apple', 'banana', 'orange', 'pear']
index = find_index(my_list, 'orange')
print(index) 
    


# ## 23. Write a Python program to flatten a shallow list. Go to the editor
# Click me to see the sample solution

# In[110]:


def flatten(list1):
    flatten_list = []
    for item in list1:
        if isinstance(item, list): # Checking item as list
            for nested_item in item:
                flatten_list.append(nested_item)
                
        else:
            flatten_list.append(item)
            
    return flatten_list

my_list = [1, [2, 3], 4, [5, 6]]
flatten_list = flatten(my_list)
print(flatten_list)

            


# ## 24. Write a Python program to append a list to the second list. Go to the editor
# Click me to see the sample solution

# In[113]:


def append_lists(list1, list2):
    
    for item in list1:
        list2.append(item)
        
my_list1 = [10, 20, 30]
my_list2 = [40, 50, 60]
append_lists(my_list1, my_list2)
print(sorted(my_list2))


# ## 25. Write a Python program to select an item randomly from a list. Go to the editor
# Click me to see the sample solution

# In[118]:


import random

my_list = [3,4,5,6,7,8,9]
random_number = random.choice(my_list)
print(random_number)

#### Another version

random_index = random.randint(0, len(my_list)-1)
random_item = my_list[random_index]
print(random_item)


# ## 26. Write a Python program to check whether two lists are circularly identical. Go to the editor
# Click me to see the sample solution

# In[66]:


def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    
    concatenated = list1 + list2
    if all(elem in concatenated for elem in list2):  # Taking a list as an example to see that everything matching 
        return True
    
    return False

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 10, 20]

if are_circularly_identical(list1, list2):
    print("The two lists are circularly identical")
else:
    print("The two lists are not circularly identical")


# ## 27. Write a Python program to find the second smallest number in a list. Go to the editor
# Click me to see the sample solution

# In[68]:


def find_second_smallest(numbers):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    return second_smallest

numbers = [23,34,56,43,21,11,43,54,67,87,42]

second_smallest = find_second_smallest(numbers)
print("The second smallest number is: ", second_smallest)


# ## 28. Write a Python program to find the second largest number in a list. Go to the editor
# Click me to see the sample solution

# In[71]:


def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

numbers = [50, 45, 32, 53, 78, 65, 31, 21]

second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)


# ## 29. Write a Python program to get unique values from a list. Go to the editor
# Click me to see the sample solution

# In[73]:


def get_unique_values(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [50, 45,50, 32,45, 53, 78, 65,65,65, 31, 21]
unique_numbers = get_unique_values(numbers)

print("The unique numbers are:", unique_numbers)


# ## 30. Write a Python program to get the frequency of elements in a list. Go to the editor
# Click me to see the sample solution

# In[86]:


def get_frequency(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

numbers = [50, 45,50, 32,45, 53, 78, 65,65,65, 31, 21]
unique_numbers = get_frequency(numbers)

print("The unique numbers are:", unique_numbers)


# In[ ]:





# In[91]:


def find_last_occurrence(list1, element):
    try: 
        last_occurence = len(list1) - 1 - list1[::-1].index(element)
        return last_occurence
    except ValueError:
        return -1   # element is not ofund from the list
    
my_list = [1, 2, 3, 4, 3, 5, 3]
last_occurrence = find_last_occurrence(my_list, 3)
print(last_occurrence) 


# # Given a list and an element, write a program to find the last occurrence of the element in the list.

# In[95]:


def last_occurrence(lst, elem):
    last_index = -1
    
    for i in range(len(lst)):
        if lst[i] == elem:
            last_index = i
    return i

my_list = [10, 20, 30, 40, 30, 20, 10]
my_element = 30
last_index = last_occurrence(my_list, my_element)
print(f"The last occurrence of {my_element} is at index {last_index}.")


# # Example 2: Set

# ## 1. Write a Python program to create a set.

# In[22]:


numbers = set()

# add numbers to the set if they are even

for i in range(1,20):
    if i % 2 == 0:
        numbers.add(i)
       
print(numbers)


# ## 2. Write a Python program to iterate over sets.

# In[23]:


sets = {2,3,4,5,6,7,8}

for num in sets:
    print("We have Printed Number in a Set: ", num)
    
# Another Version

# using a while loop and iterator
iterator = iter(x for x in sets if x % 2 == 0)

while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break


# # 3. Write a Python program to add member(s) to a set.

# In[24]:


my_set = {'apple', 'banana', 3.14, 2.718}
new_members = ['banana', 2.718, 'orange', 4.20]

for items in new_members: 
    if items not in my_set:
        my_set.add(items)
print(my_set)


# ## 4. Write a Python program to remove item(s) from a given set.

# In[25]:


my_set = {1, 2, 'apple', 'banana', 3.14, 2.718}

my_set.remove('apple')

print(my_set)

# Remove multiple items from the set
items_to_remove = {1, 'banana', 2.718}
my_set.difference_update(items_to_remove)

print(my_set) # Output {3.1416}


# ## 5. Write a Python program to remove an item from a set if it is present in the set.

# In[30]:


# create a set of numbers
numbers = {1, 2, 3, 4, 5}

# remove an item from the set if it is present
if 3 in numbers:
    numbers.remove(3)

print(numbers) # Output: {1, 2, 4, 5}


# ## 6. Write a Python program to create an intersection of sets.

# In[31]:


# Create Two Sets
set1 = {2,3,4,5,6,7,8}
set2 = {3,4,5,6,7,8,9}

# Create an empty set to store the intersection
intersection = set()

# Loop through the first set and check if each item is in the second set

for item in set1:
    if item in set2:
        intersection.add(item)
        
print(intersection)


# ## 7. Write a Python program to create a union of sets

# In[32]:


set1 = {3,4,5,6,7}
set2 = {2,3,4,5,6}

union_set = set1.copy()
for elem in set2:
    if elem not in set2:
        union_set.add(elem)
        
print(union_set)


# ## 8. Write a Python program to create set difference.

# In[33]:


set1 = {1,2,3,4,5,6,7}
set2 = {3,4,5,6,7,8,9}

diff_set = set1 - set2
print(diff_set)

# Another Version


# ## 9. Write a Python program to create a symmetric difference

# In[34]:


set1 = {1,2,3,4}
set2 = {3,4,5,6}

symmetric_diff = set()

for element in set1:
    if element not in set2:
        symmetric_diff.add(element)
        
for element in set2:
    if element not in set1:
        symmetric_diff.add(element)
        
print(symmetric_diff)

# Alternative Version

sym_diff = set1.symmetric_difference(set2)  # Using direct method
print(sym_diff)


# ## 10. Write a Python program to check if a set is a subset of another set.

# In[35]:


set1 = {5,6,7,8,9}
set2 = {6,7,8}

is_subset = True
for element in set2:
    if element not in set1:
        is_subset = False
        break

if is_subset:
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")
    
# Another Example:

set1 = {5,6,7,8,9}
set2 = {6,7,8}

if set2 <= set1:
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")
    
# Another Example 2:


if set2.issubset(set1):
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")


# ## 11. Write a Python program to create a shallow copy of sets.

# In[36]:


import copy 

set1 = {23,24,25,27,28,29,30}
set2 = {10, 23, 45, (23,32), 21} # Set2 contains only the hashable type

set3 = set1.copy()
set3 = set(set1)
set3
set4 = copy.deepcopy(set2)
set4

print(set3)
print(set4)


# In[37]:


# Loop Method
set1 = {23,24,25,27,28,29,30}
set2 = set1.copy()
set3 = set(set2)

# Check if set2 is a subset of set1

for element in set2:
    if element not in set1:
        print("Set 2 is not a subset of set 1")
        break
else:
    print("Set 2 is a Subset of Set 1")
    
# Checking If set 3 is a subset of Set 1

for element in set3:
    if element not in set1:
        print("Set3 is not a Subset of Set1")
        break
else:
    print("Set3 is Subset of Set 1")


# ## 12. Write a Python program to remove all elements from a given set.

# In[38]:


set = {2,3,4,5,6,7}

set.clear()
print(set)


# ## 13. Write a Python program that uses frozensets. Go to the editor
# Note: Frozensets behave just like sets except they are immutable.

# In[44]:


sets = {1,2,3,4,5,6,7}
frozen_set = frozenset(sets)
print(frozen_set)

# Adding element in frozen set

try:
    frozen_set.add(4)
except AttributeError:
    print("Error!")


# ## 14. Write a Python program to find the maximum and minimum values in a set.

# In[47]:


sets = {1,2,3,4,5,6,7}

max_value = max(sets)
min_value = min(sets)
print(max_value)
print(min_value)


#  ## 15. Write a Python program to find the length of a set.

# In[50]:


my_set = {1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15}

length = len(my_set)
print("Length of set:", length)


# ## 16. Write a Python program to check if a given value is present in a set or not. 

# In[54]:


my_set = {1, 2, 3, 4, 5, 6, 7,    ;     8}

if 8 in my_set:
    print("8 is in set")
else:
    print("8 not in the set")
    
if 2 in my_set:
    print("2 is present")
else:
    print("2 is not present")


# ## 17. Write a Python program to check if two given sets have no elements in common. 

# In[57]:


set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

if set1.isdisjoint(set2):
    print("Sets have no common elements")
else:
    print("Sets have common elements")
    
# ANother example

def have_no_common(set1, set2):
    if set1.isdisjoint(set2):
        return True
    else:
        return False

set1 = {1, 2, 3,4, 5}
set2 = {6, 7, 8, 9, 10}


if have_no_common(set1, set2):
    print("Sets have no common elements")
else:
    print("Sets have common elements")
    


# ## 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set. 

# In[58]:


set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

if set1.issuperset(set1) and set1.issuperset(set2):
    print("Set 1 is a superset of itself and set2")
else:
    print("Set 1 is not a superset of itself and set2")
    


# ## 19. Write a Python program to find elements in a given set that are not in another set.

# In[60]:


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
diff_set = set1.difference(set2)
diff_set


# ## 20. Write a Python program to remove the intersection of a second set with a first set.

# In[24]:


first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}

first_set -= second_set.intersection(first_set)  # -= using for removing the intersection of a second set

print(first_set)


# ## 21. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type

# In[6]:


list_of_strings = ["There are", "numerous entity", "that gives you wings", "are wings"]

word_count = {}

for string in list_of_strings:
    words = set(string.split())
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
unique_words = set(word_count.keys())

print("Unique Words: ")
for word in unique_words:
    print(word)
    
print("\nWord Frequency (Count for each word): ")
for word, count in word_count.items():
    print(word, count)
    
    


# ## 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value. 

# In[15]:


def pairs(nums, end_sum):
    list_of_pairs = []
    for i in range(len(nums)):   # whenever applying range(len()) process we are working with both idex and its associated value like enumeration
        for j in range(i+1, len(nums)):  # i+1 going for j presenting the second element value
            if nums[i] + nums[j] == end_sum:  # firsta and second element addition is 9 
                list_of_pairs.append((nums[i], nums[j]))
    return list_of_pairs

nums = [1,2,3,4,5,6,7,8,9]
end_sum = 9
pair = pairs(nums, end_sum)
print(pair)
print(f"List of pairs whose sum is equal to a given value {end_sum} is: {pair}")


# ## 23. Write a Python program to find the longest common prefix of all strings. Use the Python set.

# In[27]:


def longest_common_prefix(string):
    
    if not string:
        return ""
    
    prefix = string[0]
    for s in string[1:]:
        while prefix != s[:len(prefix)]:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strings = ["loevebirdd", "loewer feelingss", "loew budgett"]
prefix = longest_common_prefix(strings)
print(prefix)  

# Another Version

def longest_common_prefix(string):
    if not string:
        return ""
    
    min_length = min([len(word) for word in string])  # This becomes the maximum length of the common prefix that can exist among all the strings.
    for i in range(min_length): # it loops over the indices from 0 to min_length - 1 and for each index, it extracts the character at that index from all the strings in the list using a list comprehension
        chars = set([word[i] for word in string]) # set function creates a set of unique characters
        if len(chars) >  1: # f the length of the set is greater than 1, it means that the character at that index is not common to all the strings in the list and the function returns the common prefix up to the previous index using slicing
            return string[0][:i]  # Including zero to zero to ith value
    return string[0][:min_length]  #  All the characters up to the minimum length are common to all the strings. 

names = ["Robabu", "Robust", "Roshun"]
n = longest_common_prefix(names)
print(n)


# ## 24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set. 

# In[28]:


def max_product(nums):
    if len(nums) < 2: # First checks if the list has at least 2 numbers
        return None
    
    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)  # It finds the maximum number in the remaining list (which now doesn't have max1) and assigns it to the variable max2
    return max1 * max2

num = [2,3,4,5,6]
max_product = max_product(num)
print(max_product)


# ## 25. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

# In[29]:


def missing_numbers(set1, set2):
    set1_diff = set1.difference(set2)
    set2_diff = set2.difference(set1)
    return set1_diff, set2_diff

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 7, 9}
set1_diff, set2_diff = missing_numbers(set1, set2)
print(set1_diff) 
print(set2_diff)  


# ## 26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

# In[38]:


def group_anagrams(words):
    groups = {}  # empty dictionary called groups
    for word in words:
        sorted_word = ''.join(sorted(word)) # sorts its letters in alphabetical order using the sorted function. It joins the sorted letters back into a string using the join method
        if sorted_word not in groups:  # If sorted_word is not already a key in the groups dictionary, the function creates a new empty list as its value
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    return list(groups.values())

words = ['apple', 'elppa', 'bat', 'atb', 'eat', 'tea', 'ate']
anagrams_groups = group_anagrams(words)
print(anagrams_groups)
        


# In[ ]:





# ## 27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.

# In[75]:


def group_anagrams(strings):
    final = {}
    for x in strings:
        sorted_string = ''.join(sorted(x))
        if sorted_string not in final:
            final[sorted_string] = [x]  # Different code than previous one
        else:
            final[sorted_string].append(x) 
    return list(final.values())

strings = ['eat', 'cba', 'tae', 'abc', 'xyz', 'yzx']
print(strings)
print(group_anagrams(strings))


# ## 28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number. 

# In[80]:


from itertools import combinations

# Define function to find all combinations of 3 numbers from a given list
def find_combination(numbers, target):
    
    # Create empty list to store the results
    results = []
    #Loop through all combinations of 3 numbers from the 'number' list
    for combination in combinations(numbers, 3):
        # Check if the sum of the 3 numbers equals the target number
        if sum(combination) == target:
            # If it does, append the combination to the results list
            results.append(combination)
            
    return results

# Define a list of numbers and a target number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

# Call the 'find_combinations' function with the list of numbers and target number
combinations = find_combination(numbers, target)

print(combinations)
    


# ## 29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type. 

# In[102]:


def find_third_largest(numbers):
    unique = set(numbers)
    
    # If there are fewer than 3 unique numbers, return None
    if len(numbers) < 3:
        return None
    
    # Otherwise convert the set back to a list and sort it in descending order
    sorted_num = sorted(unique, reverse=True)
    print(f"Sorted Number: {sorted_num} ")
    
    return f'Third Largest Number is: {sorted_num[2]}'

numbers = [34, 21, 35, 43, 52, 68, 89, 14, 71]
third_largest = find_third_largest(numbers)
print(third_largest) # Output: 7


# ## 30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.

# In[101]:


def remove_duplicates(strings):
    unique_strings = []
    for string in strings:
        if string not in unique_strings:
            unique_strings.append(string)
    return unique_strings

strings = ['batman', 'superman', 'spiderman', 'batman', 'superman', 'antman']
unique_strings = remove_duplicates(strings)
count = len(unique_strings)
print("Unique strings:", unique_strings)
print("Count of unique strings:", count)


# # ***** Example 3: Tuple

# ## 1. Write a Python program to create a tuple.

# In[26]:


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)


# ## 2. Write a Python program to create a tuple with different data types.

# In[27]:


# Different data types
my_tuple = ("hello", 234, 31.14, False)
print(my_tuple)


# ## 3. Write a Python program to create a tuple of numbers and print one item. 

# In[28]:


# tuple of numbers
my_tuple = (10, 20, 30, 40, 50)

# Printing one item from the tuple
print(my_tuple[2:5], my_tuple[3])


# ## 4. Write a Python program to unpack a tuple into several variables. 

# In[29]:


my_tuple = (11, 22, 33, 44, 55, 66, 77)
a, b, c, d, e, f, g = my_tuple

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)
print("g:", g)

# Another Format

# Unpacking using loop

for item in my_tuple:
    print("Item is: ", item)
    
# Or

for item in enumerate(my_tuple):
    print("Item is: ", item)


# ## 5. Write a Python program to add an item to a tuple.

# In[30]:


"""tuples in Python are immutable, meaning their elements cannot be modified after creation."""

# tuple concatenation Method:

my_tuple = (11, 22, 33, 44, 55, 66)

# Item to be added
new_item = 8

# Create a new tuple with the additional item using tuple concatenation
new_tuple = my_tuple + (new_item,)
print(new_tuple)


# ## 6. Write a Python program to convert a tuple to a string.

# In[31]:


my_tuple = (11, 22, 33, 44, 55, 66)
string = ''.join(str(element) for element in my_tuple)
print("Connverted String of Tuple: ", string)

# Another Method
# Convert tuple to string using string formatting
tuple_string = str(my_tuple)

# Print the string representation of the tuple
print("Tuple as string:", tuple_string)


# ## 7. Write a Python program to get the 4th element from the last element of a tuple.

# In[32]:


my_tuple = (11, 22, 33, 44, 55, 66)

# Get the 4th element from the last element of the tuple
fourth = my_tuple[-4]

# Print the element
print("4th element from the last:", fourth)


# ## 8. Write a Python program to create the colon of a tuple.

# In[33]:


import copy

# Create a tuple
tuplex = (10, 20, [30, 40], 50, 60)

# Print the original tuple
print("Original tuple:", tuplex)

# Create a deep copy of the tuple using deepcopy()
tuplex_copy = copy.deepcopy(tuplex)

# Modify the deep copied tuple
tuplex_copy[2].append(80)

# Print the deep copied tuple
print("Deep copied tuple:", tuplex_copy)

# Print the original tuple after modifying the deep copied tuple
print("Original tuple after deep copy:", tuplex)


# ## 9. Write a Python program to find repeated items in a tuple.

# In[34]:


# version 1:

def repeated_item(tuplex):
    repeated_items = []
    for item in tuplex:
        if tuplex.count(item) > 1 and item not in repeated_items:  # distinct numbers count to find the repeated value
            repeated_items.append(item)
    return repeated_items

my_tuple = (11, 22, 33, 44, 55, 22, 66, 55)

repeated_items = repeated_item(my_tuple)

print("Repeated items are:", repeated_items)

# Version 2:

def repeated_item(tuplex):
    repeated_items = []
    for item in tuplex:
        count = 0
        for element in tuplex:
            if element == item:
                count += 1
        if count > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

repeated_items = repeated_item(my_tuple)

print("Repeated items are:", repeated_items)


# ## 10. Write a Python program to check whether an element exists within a tuple.

# In[35]:


def check_element_exists(tuplex, element):
    if element in tuplex:
        return True
    else:
        return False

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Check if element 3 exists in the tuple

if check_element_exists(my_tuple, 3):
    print("Element 3 exists in the tuple.")
else:
    print("Element 3 does not exist in the tuple.")

# Check if element 6 exists in the tuple
if check_element_exists(my_tuple, 6):
    print("Element 6 exists in the tuple.")
else:
    print("Element 6 does not exist in the tuple.")


# ## 11. Write a Python program to convert a list to a tuple.

# In[36]:


my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print(my_tuple)


# ## 12. Write a Python program to remove an item from a tuple.

# In[37]:


# Tuples are immutable, which means that their contents cannot be modified.

my_tuple = (10,20,30,40,50,60,70)
remove_item = 40

new_tuple = tuple(item for item in my_tuple if item != remove_item)
new_tuple

########################
my_tuple = (10,20,30,40,50,60,70)
remove_item = (40,50,60)

new_tuple = tuple(item for item in my_tuple if item not in remove_item)
new_tuple


# ## 13. Write a Python program to slice a tuple.

# In[38]:


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slice the tuple from index 2 to index 5 (exclusive)
slice_tuple = my_tuple[2:5]

print(slice_tuple)


# ## 14. Write a Python program to find the index of an item in a tuple.

# In[39]:


my_tuple = (1,2,3,4,5,6,7)
item_to_find = 4

if item_to_find in my_tuple:
    index = my_tuple.index(item_to_find)
    print(f"The index of {item_to_find} in {my_tuple} is {index}")
else:
    print(f"{item_to_find} is not in {my_tuple}")


# ## 15. Write a Python program to find the length of a tuple.

# In[40]:


my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)

print(f"The length of {my_tuple} is {length}")


# ## 16. Write a Python program to convert a tuple to a dictionary.

# In[41]:


my_tuple = (("apple", 3), ("banana", 2), ("orange", 1))
my_dict = dict(my_tuple)

print(f"The tuple {my_tuple} converted to a dictionary is {my_dict}")


# ## 17. Write a Python program to unzip a list of tuples into individual lists.

# In[42]:


my_list = [(1, "apple"), (2, "banana"), (3, "orange")]

"""
zip function with the * operator to unzip the list into two separate lists: 
one containing the numbers and one containing the fruits.
"""

numbers, fruits = zip(*my_list)  
print(f"The list {my_list} unzipped into {numbers} and {fruits}")


# ## 18. Write a Python program to reverse a tuple.

# In[43]:


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)


# ## 19. Write a Python program to convert a list of tuples into a dictionary.

# In[44]:


my_list = [("sakib", 3), ("robin", 2), ("shafee", 1)]
my_dict = dict(my_list)
my_dict


# ## 20. Write a Python program to print a tuple with string formatting. Go to the editor
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)

# In[45]:


my_tuple = (100, 200, 300)
print(f"This is a tuple {my_tuple}")


# ## 21. Write a Python program to replace the last value of tuples in a list. Go to the editor
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# In[46]:


my_tuple = (100, 200, 300)
print(f"This is a tuple {my_tuple}")


# ## 22. Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# In[47]:


my_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list = [t for t in my_list if t]

print(f"The original list was {my_list} and the new list is {new_list}")


# ## 23. Write a Python program to sort a tuple by its float element. Go to the editor
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

# In[48]:


my_tuple = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

sorted_tuple = sorted(my_tuple, key=lambda x: float(x[1]), reverse=True) #x[1] is the positon of the second element floating points for each tuple
print(sorted_tuple)


# ## 24. Write a Python program to count the elements in a list until an element is a tuple

# In[49]:


my_list = [12, 23, 'mushfiq', (4, 5), 6, 'seven', (9, 10)]
count = 0

for item in my_list:
    if isinstance(item, tuple):  # isinstance function to check if the current item is a tuple.
        break
    count += 1
print(f"The number of elements in the list before a tuple is found: {count}")


# ## 25. Write a Python program to convert a given string list to a tuple. Go to the editor
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# <class 'tuple'>

# In[61]:


string_list = ['python', '3.0']

# Join the strings in the list to create a single string
joined_string = ''.join(string_list)  # join() method. In this case, we use an empty string '' as the separator between each element of the list.
tuple_string = tuple(joined_string)

print(f"Original string: {joined_string}\n{type(joined_string)}")
print(f"Convert the said string to a tuple:\n{tuple_string}\n{type(tuple_string)}")


# ## 26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple. Go to the editor
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

# In[62]:


def tuple_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tup1 = (4, 3, 5, 6, -1, -4, 10)
tup2 = (2, 3, 4, -6, -5, 12, 1)
print(f"Product 1 Output: {tuple_product(tup1)}")
print(f"Product 1 Output: {tuple_product(tup2)}")


# ## 27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples. Go to the editor
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]

# In[63]:


def average_tuple_tuples(t):
    
    # Determine the number of columns (n) and rows (m) in the tuple of tuples
    n = len(t[0])
    m = len(t)
    
    # creating empty list to store the average value
    result = []
    
    # Iterate over eah column of the tuple of tuples
    for i in range(n):
    # Initializing a variable to store the sum
        sum = 0
        
        # Iterate over each row of the tuples of tuples and add the number in the current column to the sum
        for j in range(m):
            sum += t[j][i]  # sum += t[j][i] in this code adds the value in the i-th column and j-th row of the tuple of tuples to the sum. 
            
        # Calculate the average value of the numbers in the current column and append
        result.append(sum/m)
        
    return result

t1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print("Original Tuple:")
print(t1)
print("Average value of the numbers of the said tuple of tuples:")
print(average_tuple_tuples(t1))

t2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print("\nOriginal Tuple:")
print(t2)
print("Average value of the numbers of the said tuple of tuples:")
print(average_tuple_tuples(t2))


# ## 28. Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

# In[64]:


def strings_to_integer(t):
    return tuple(tuple(int(s) for s in tup) for tup in t)

t1 = (('333', '33'), ('1416', '55'))
print(f"convert a tuple of string values to a tuple of integer values: {strings_to_integer(t1)}")


# ## 29. Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

# In[65]:


def tuple_to_int(t):
    
    # converting each element of the tuple to a string and concatenate them
    a = ''.join(str(i) for i in t)
    # covert the result string to an integer as a whole
    return int(a)

t1 = (1, 2, 3)
print(f"tuple of positive integers into an integer: {tuple_to_int(t1)}")  

t2 = (10, 20, 40, 5, 70)
print(f"tuple of positive integers into an integer: {tuple_to_int(t2)}") 


# ## 30. Write a Python program to check if a specified element appears in a tuple of tuples. Go to the editor
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White present in said tuple of tuples!
# True
# Check if White present in said tuple of tuples!
# True
# Check if Olive present in said tuple of tuples!
# False

# In[85]:


def element_in_tuple(element, tuple_of_tuples):
    for tup in tuple_of_tuples:
        if element in tup:
            return True
    return False

t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
print(element_in_tuple('White', t))
print(element_in_tuple('Pink', t))
print(element_in_tuple('Olive', t))

# Alternative Method

color = [ ]


# 

# In[ ]:





# # ***** Example 4: Dictionary

# ## 1. Write a Python script to sort (ascending and descending) a dictionary by value. 

# In[124]:


my_dict = {'hassan': 5, 'banna': 2, 'kobir': 10, 'sumon': 4}
sort_dict_ascen = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=False))
sort_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sort_dict)
print(sort_dict_desc)


# ## 2. Write a Python script to add a key to a dictionary. 

# In[127]:


my_dict = {'sakib': 3, 'asif': 5}
my_dict['robin'] = 4
my_dict


# ## 3. Write a Python script to concatenate the following dictionaries to create a new one.

# In[135]:


dict1 = {'sakib': 15, 'robin': 91}
dict2 = {'hassan': 25, 'karim': 99}

concat_dict = {**dict1, **dict2}
print(concat_dict)

concat_dict1 = dict1.copy()
concat_dict1.update(dict2)
print(concat_dict1)


# ## 4. Write a Python script to check whether a given key already exists in a dictionary. 

# In[137]:


my_dict = {'name': 'Sakib', 'age': 25, 'capital': 'Dhaka'}

check = 'age'  # I should check the key value 

if check in my_dict:
    print(f"The Key {check} exists in the dictionary")
else:
    print(f"The key {check} does not exist in the dictionary")


# ## 5. Write a Python program to iterate over dictionaries using for loops.

# In[139]:


my_dict = {'name': "John", 'age': 50, 'city': 'Dhaka'}


for key in my_dict:
    print(key)
    
for value in my_dict.values():
    print(value)
    
for key, value in my_dict.items():
    print(f"{key}: {value}")


# ## 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# In[143]:


n = int(input("Enter a Number: "))
my_dict = {}

for i in range(1, n+1):
    my_dict[i] = i*i
    
print(my_dict)


# ## 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# In[146]:


my_dict = {}

for i in range(1, 16):
    my_dict[i] = i*i

print(my_dict)


# ## 8. Write a Python script to merge two Python dictionaries.

# In[145]:


dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged_dict = {**dict1, **dict2}

print(merged_dict)


# ## 9. Write a Python program to iterate over dictionaries using for loops.

# In[148]:


my_dict = {"apple": 2, "banana": 3, "orange": 4, "peach": 5, "watermelon": 6, "kiwi": 7, "pineapple": 8,
           "pear": 9, "grape": 10}

# Iterate over keys

for key in my_dict:
    print(key)
    
for value in my_dict.values():
    print(value)

# Iterate over the items (key-value pairs) of the dictionary
for key, value in my_dict.items():
    print(key, value)


# ## 10. Write a Python program to sum all the items in a dictionary. 

# In[155]:


my_dict = {"gpu": 22, "cpu": 30, "motherboard": 14, 'monitor': 33}

sum_val = sum(my_dict.values())
print(f"sum of all values in dictionary: {sum_val}")


# ## 11. Write a Python program to multiply all the items in a dictionary. 

# In[156]:


my_dict = {"gpu": 22, "cpu": 30, "motherboard": 14, 'monitor': 33}

product = 1
for value in my_dict.values():
    product *= value
    
print(f"The Product of all the values in the dictionary is: {product}")


# ## 12. Write a Python program to remove a key from a dictionary. 

# In[158]:


my_dict = {"gpu": 22, "cpu": 30, "motherboard": 14, 'monitor': 33}

del my_dict["cpu"]
print(my_dict)


# ## 13. Write a Python program to map two lists into a dictionary.

# In[161]:


keys = ['gpu', 'cpu', 'ssd card']
values = [4,5,6]

my_dict = dict(zip(keys, values))  # zip providing mapping for key and value lists and coverting them into dictionary
print(my_dict)


# ## 14. Write a Python program to sort a given dictionary by key.

# In[162]:


my_dict = {"gpu": 22, "cpu": 30, "motherboard": 14, 'monitor': 33}

sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)


# ## 15. Write a Python program to get the maximum and minimum values of a dictionary.

# In[168]:


my_dict = {"gpu": 22, "cpu": 30, "motherboard": 14, 'monitor': 33, 'ram': 45}

def get_max(dict1):
    max_value = float('-inf') #  special floating-point value that represents negative infinity.
    for value in dict1.values():
        if value > max_value:
            max_value = value
    return max_value

def get_min(dict1):
    min_value = float('inf')
    for value in dict1.values():
        if value < min_value:
            min_value = value
    return min_value

max_value = get_max(my_dict)
min_value = get_min(my_dict)
print(max_value)
print(min_value)

### Alternative Method using None data dtype

def get_max(dict1):
    max_value = None
    for value in dict1.values():
        if max_value is None or value > max_value:
            max_value = value
    return max_value

def get_min(dict1):
    min_value = None
    for value in dict1.values():
        if min_value is None or value < min_value:
            min_value = value
            
    return min_value

max_value = get_max(my_dict)
min_value = get_min(my_dict)
print(max_value)
print(min_value)


# ## 16. Write a Python program to get a dictionary from an object's fields. 

# In[174]:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
person = Person("Sakb", 25, "Zigatola,Dhaka")
dict_person = vars(person)
print(dict_person)

# More complex version

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
person = Person("Sakib", 25, "Zigatola,Dhaka")

def object_to_dict(obj):
    obj_dict = {}
    for attributes in dir(obj):
        if not attributes.startswith("__"):
            obj_dict[attributes] = getattr(obj, attributes)
        
    return obj_dict

person_dict = object_to_dict(person)

print(person_dict)


# ## 17. Write a Python program to remove duplicates from the dictionary. 

# In[29]:


d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

new_dict = {}

for key, value in d.items():
    if value not in new_dict.values():
        new_dict[key] = value
        
print("New Dictionary after Removing duplicates in values part: ", new_dict)


# ## 18. Write a Python program to check if a dictionary is empty or not.

# In[81]:


a = {}

# Check if the dictionary is empty or not
if not a:
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")


# ## 19. Write a Python program to combine two dictionary by adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# In[82]:


from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

combined = Counter(d1) + Counter(d2)
print(combined)

# Alternative Method: 

def combine_dicts(d1, d2):
    combine = {}
    
    for key in d1:
        if key in d2:
            combine[key] = d1[key] + d2[key]
        else:
            combine[key] = d1[key]
            
    
    for key in d2:
        if key not in d1:
            combine[key] = d2[key]
    return combine

combine = combine_dicts(d1, d2)

# Print the combined dictionary
print("Using after USer Defined Function: ", combine)


# ## 20. Write a Python program to print all distinct values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# In[43]:


data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_values = set()  # set() data type in Python is designed to store unique values only. 
                        # When you add a value to a set that is already in the set, the set does not add it again.

for d in data:
    for value in d.values():
        unique_values.add(value)
        
print("Unique Values: ", unique_values)


# ## 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# In[84]:


import itertools

data = {'1':['a', 'b'], '2': ['c','d']}
letter_lists = [data[k] for k in sorted(data.keys())]
combinations = list(itertools.product(*letter_lists))

for combination in combinations:
    print(''.join(combination))


# ## 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary

# In[109]:


my_dict = {'a': 300, 'b': 200, 'c': 500, 'd': 100, 'e': 700, 'f': 200}
values = list(my_dict.values())
values.sort(reverse=True)
top_3_values = values[:3]

top_3_keys = []
for key, value in my_dict.items():
    if value in top_3_values:
        top_3_keys.append(key)
        
print("Highest Three Value in Dictionary: ")
for i in range(len(top_3_keys)):
    print("{}: {}".format(top_3_keys[i], top_3_values[i]))
    


# ## 23. Write a Python program to combine values in a list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

# In[113]:


from collections import defaultdict

data =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combine = defaultdict(int)
for d in data:
    combine[d['item']] += d['amount']  # The default value is 0 
                                        # so there is no need to  
                                        # enter the key first 
    
print(dict(combine))

# Another Method

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = {}
for d in data:
    item = d['item']
    amount = d['amount']
    
    """ These lines check if the item key already exists in the result dictionary. 
    If it does, the amount value is added to the existing value.
    If it doesn't, a new key-value pair is created with the item as the key and the amount as the value. """
    
    if item in result:
        result[item] += amount
    else:
        result[item] = amount

print(result)


# ## 24. Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# In[1]:


string = 'w3resource'

letter_count = {}

for char in string:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
        
print(letter_count)


# ## 25. Write a Python program to print a dictionary in table format.

# In[135]:


# First Version:

dict_values = {'alpha':[2,4,6,8,10], 'gamma': [12,14,16,18,20], 'sigma': [22,24,26,28,30]}

print("Raw Version: ")
for row in zip(*([key] + (value) for key, value in sorted(dict_values.items()))):
    print(*row)
    
# I wanna uses tabulate to print the dictionary as a table using fancy_grid

from tabulate import tabulate

dict_values = {'alpha':[2,4,6,8,10], 'gamma': [12,14,16,18,20], 'sigma': [22,24,26,28,30]}

headers = ['key'] + list(dict_values.keys())
rows = []
for i in range(len(list(dict_values.values())[0])):
    row = []
    for key in headers:
        if key == 'key':
            row.append(list(dict_values.values())[0][i])
        else:
            row.append(list(dict_values.values())[list(dict_values.keys()).index(key)][i])
            
    rows.append(row)
    
print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
            


# For more information about tabulate: https://openbase.com/python/tabulate/documentation

# ## 26. Write a Python program to count the values associated with a key in a dictionary.

# In[11]:


def count_key_in_dict(key, dict_val):
    count = 0
    for k in dict_val.keys():
        if k == key:
            count += 1
    return count

dict_val = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(count_key_in_dict('a', dict_val)) # Output: 1
print(count_key_in_dict('b', dict_val)) # Output: 1
print(count_key_in_dict('c', dict_val)) # Output: 1
print(count_key_in_dict('d', dict_val)) # Output: 1
print(count_key_in_dict('e', dict_val)) 

# Class-Object Method:

class DictCounter:
    def __init__(self, dict_values):
        self.dict_values = dict_values
        
    def count_key_in_dict(self, key):
        count = 0
        for k in self.dict_values.keys():
            if k == key:
                count += 1
        return count
    
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
counter = DictCounter(my_dict)
print(counter.count_key_in_dict('a')) # Output: 1
print(counter.count_key_in_dict('b')) # Output: 1
print(counter.count_key_in_dict('c')) # Output: 1
print(counter.count_key_in_dict('d')) # Output: 1
print(counter.count_key_in_dict('e')) # Output: 0
    


# ## 27. Write a Python program to convert a list into a nested dictionary of keys.

# In[15]:


def list_to_nested_dict(list1):
    result = {}
    current_dict = result
    
    for key in list1:
        current_dict[key] = {}
        current_dict = current_dict[key]
    return result


my_list = ['a', 'b', 'c', 'd']
print(list_to_nested_dict(my_list))

# Alternative Method(object oriented)

class NestedDict:
    def __init__(self):
        self.dictionary = {}

    def add_keys(self, keys):
        current_dict = self.dictionary
        for key in keys:
            current_dict[key] = {}
            current_dict = current_dict[key]

    def get_dict(self):
        return self.dictionary

# Example usage
my_list = ['a', 'b', 'c', 'd']
nd = NestedDict()
nd.add_keys(my_list)
print(nd.get_dict()) # Output: {'a': {'b': {'c': {'d': {}}}}}}


# ## 28. Write a Python program to sort a list alphabetically in a dictionary.

# In[81]:


my_dict = {'banana': 3, 'apple': 2, 'orange': 4, 'grape': 1}

sorted_list = sorted(my_dict.items(), key=lambda x: x[0])
print(sorted_list)


# ## 29. Write a Python program to remove spaces from dictionary keys.

# In[82]:


my_dict = {'banana lorry': 3, 'apple pie': 2, 'orange cake': 4, 'grape juice': 1}

new_dict = {}
for key, value in my_dict.items():
    new_key = key.replace(" ", "")
    new_dict[new_key] = value
    
print(new_dict)


# ## 30. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}a
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# In[83]:


shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

sorted_items = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)  # accessing to the values and sorted them asending order
top_three_items = sorted_items[:3] # 0,1,2 not including 3 index position

for item in top_three_items:
    print(f"{item[0]} {item[1]}")


# # *****Example 5: List Comprehension
#     

# ## 1. Write a Python function to reverse a list at a specific location.

# In[1]:


def reverse_list_at_location(list1, index):
    """
     the list to be reversed and the index at which the reversal should start. 
     It first slices the list from the beginning up to the specified index
    """
    return list1[:index] + [i for i in reversed(list1[index:])] # it concatenates the two lists using the + operator and returns the result.

my_list = [1,2,3,4,5,6,7,8]
print(reverse_list_at_location(my_list, 2))


# ## 2. Write a Python function find the length of the longest increasing sub-sequence in a list.

# In[3]:


def longest_increasing_subsequence_length(numbers):
    n = len(numbers)
    array = [1] * n
    for i in range(1,n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                array[i] = max(array[i], array[j]+1)
    return max(array)

numbers = [10,20,30,40,50,60]
print("Length of the longest increasing sub-sequence: ", longest_increasing_subsequence_length(numbers))


# ## 3. Write a Python function that finds all the permutations of the members of a list.

# In[7]:


from itertools import permutations

def find_permutation(lst):
    return [p for p in permutations(lst)]

lst = [3,4,5,6]
print(find_permutation(lst))


# ## 4. Write a Python function to find the kth smallest element in a list.

# In[13]:


def kth_smallest_number(lst, k):
    """ This function takes a list and an integer k as its input. It first uses the sorted() function to sort the list in 
    ascending order, and then returns the element at the kth index (which is k-1 since Python lists are zero-indexed).
    """
    
    return sorted(lst)[k-1]

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(lst))
k = 4
kth = kth_smallest_number(lst, k)
print(f"The {k}th smallest element in {lst} is {kth}.")


# ## 5. Write a Python function to find the kth largest element in a list. 

# In[84]:


def kth_largest(lst, k): 
    return sorted(lst, reverse=True)[k-1] # rveerses true means anfter sorted the list it will go like 5,4,3,2,1 and k-1 first and quickly returns the largest value at the end of the list

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 2
kth = kth_largest(lst, k)
print(f"The {k}nd largest element in {lst} is {kth}.")


# ## 6. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

# In[85]:


# Method 1:

def is_palindrome(lst):
    
    reversed_list = [lst[i] for i in range(len(lst)-1,-1,-1)]  # start, stop, step
    return lst == reversed_list

lst1 = [1, 2, 3, 2, 1]
lst2 = [1, 2, 3, 4, 5]
print(is_palindrome(lst1))  
print(is_palindrome(lst2)) 


# ## 7. Write a Python a function to find the union and intersection of two lists. 

# In[86]:


def find_union_intersection(lst1, lst2):
    union = [x for x in lst1] + [x for x in lst2 if x not in lst1]
    
    intersection = [x for x in lst1 if x in lst2]
    return (union, intersection)
    
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print(find_union_intersection(lst1, lst2))


# ## 8. Write a Python function to remove duplicates from a list while preserving the order. 

# In[87]:


def remove_duplicates(lst):
    
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
            
    return result

lst = [1, 2, 3, 2, 1, 4, 5, 3]
result = remove_duplicates(lst)
print(result)  

# Another Method

def remove_duplicates(lst):
    return [x for i,x in enumerate(lst) if x not in lst[:i]] # From the beginning to ith index value
    """
    Note that we use the enumerate function to get both the item x and the current index i in the original list lst. 
    We also use slicing to get the part of the list that comes before the current index lst[:i] and check if the item 
    x appears in this part of the list.
    """
lst = [1, 2, 3, 2, 1, 4, 5, 3]
result = remove_duplicates(lst)
print(result)


# ## 9. Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value. 

# In[88]:


def max_sum_subsequence(lst):
    
    max_sum = 0
    current_sum = 0
    for in range(len(lst)):
        current_sum += lst[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_sum_subseq(lst)
print(max_sum) 

# Another Method: Brute Force Algo

def max_sum_subsequence(lst):
    
    max_sum = lst[0]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            currnet_sum = sum(lst[i:j+1]) # +1 give full length 
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_sum_subseq(lst)
print(max_sum)




# ## 10. Write a Python a function to find the minimum sum sub-sequence in a list. Return the sub-sequence.

# In[89]:


def min_sum_subsequence(lst):
    
    min_sum = lst[0]
    min_seq = [lst[0]]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_sum = sum(lst[i:j+1])
            if current_sum < min_sum:
                min_sum = current_sum
                min_seq = lst[i:j+1]
    return min_seq

lst = [1, -2, 3, -4, 5, -6, 7, -8]
min_seq = min_sum_subsequence(lst)
print(min_seq)

# Another Method: 

def min_sum_subsequence(lst):
    """
    Finds the minimum sum sub-sequence in a list and returns the sub-sequence.
    """
    min_sum = lst[0]
    min_seq = [lst[0]]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_seq = lst[i:j+1]
            current_sum = sum(current_seq)
            if current_sum < min_sum:
                min_sum = current_sum
                min_seq = current_seq
    return min_seq

lst = [1, -2, 3, -4, 5, -6, 7, -8]
min_seq = min_sum_subsequence(lst)
print(min_seq)


# ## 11. Write a Python function to find the longest common sub-sequence in two lists.

# In[90]:


def LCS(lst1, lst2):
    
    lcs_len = 0
    
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                
                """ Whenever a match is found, the function "truncates" the prefix of lst2 up to the matching element so that 
                future matches only occur on suffixes. This approach assumes that the elements of the input lists are 
                hashable and unique. """
                lcs_len += 1
                lst2 = lst2[j+1:]
                break
    lcs = [elem for elem in lst1 if elem in lst2]
    
    return lcs

lst1 = [1,2,3,4]
lst2 = [2,3,4,8]
print(LCS(lst1, lst2))

# Another method using recursion

def LCS(lst1, lst2):
    m, n = len(lst1), len(lst2)
    if m == 0 or n == 0:
        return 0

    if lst1[m-1] == lst2[n-1]:
        return 1 + LCS(lst1[:m-1], lst2[:n-1])
    else:
        return max(LCS(lst1[:m-1], lst2), LCS(lst1, lst2[:n-1]))

lst1 = ['b','d']
lst2 = ['b', 'c', 'd']

print(LCS(lst1, lst2))  # Output: 2


# ## 12. Write a Python program to find the first non-repeated element in a list.

# In[91]:


def first_non_repeated_element(lst):
    count = {elem: lst.count(elem) for elem in lst}
    non_repeated = [elem for elem in lst if count[elem] == 1]
    return non_repeated[0] if non_repeated else None

lst = [1, 2, 3, 2, 1, 4, 4, 5]
print(first_non_repeated_element(lst)) 


# In[ ]:





# ## 14. Write a Python function to sort a list of dictionaries based on values of a key.

# In[92]:


def sort_dict_list(lst, key):
    return sorted(lst, key= lambda x: x[key])

lst = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 25}
 ]

print(sort_dict_list(lst, 'name'))



# ## 15. Write a Python program to find all the pairs in a list whose sum is equal to a given value.

# In[93]:


def find_pairs(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] + lst[j] == target]

lst = [1,2,3,4,5,6,7,8]
target = 12
pairs = find_pairs(lst, target)
print(pairs)

