"""
The below program explains about list data structure

If we want to represent a group of values as a single entity which is mutable where

    1. insertion order is preserved
    2. duplicates are allowed
    3. heterogeneous objects are allowed (meaning different types of objects)

then we should use list data structure
Lists are represented using square brackets
"""

list1 = []  # lists are represented using square brackets
print(f'The type of the variable list1 is: {type(list1)}')
list1.append(10)  # append method is used to add element to list
list1.append(20)
list1.append(30)
list1.append(10)
list1.append('dharani')
list1.append(None)  # we can append None as well to list
print(f'The elements in list1 is: {list1}')
list1[0] = 999  # since list objects are mutable we can change the values like this
print(f'Accessing first element of a list using index: {list1[0]}')
print(f'Accessing last element of a list using negative index: {list1[-1]}')
sliced_list = list1[1:4]  # we can use slice operator on lists
print(f'list1[1:4] = {sliced_list}')
list1.remove(30)  # removing an element from list
print(f'list1 after remove method is: {list1}')
print(f'The repetition operator on lists: {list1 * 2}')  # we can apply * on lists

sample_num_list = list(range(10, 100, 5))  # We can use list function to create a list out of any sequence
print(f'sample_num_list = {sample_num_list}')

sample_num_list = list('Dharani')
print(f'sample_str_list = {sample_num_list}')

nested_list = [10, 20, [30, 40]]
print(f'Accessing nested list element using index: {nested_list[2]}')
print(f'Accessing second element in nested list element using index: {nested_list[2][1]}')

# Traversing through elements of a list
# We can use for loop and while loop to traverse through elements of list

list1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
for x in range(len(list1)):
    print(f'The character {list1[x - len(list1)]} is present at +ve index {x} and at -ve index {x - len(list1)}')

'''
Difference between functions and methods:
-----------------------------------------

As Python is both functional and object-oriented programming language.
Functions we define outside the class are known as functions only
Functions we define inside the class are called methods.

'''

# Important functions and methods of list

'''

1. len(list) -- to know the number of elements in the list
2. l.count(element) -- to know the number of occurrences of the substring we passed
3. l.index(element) -- return the first occurrence of the element we specify
                       If the specified element doesn't exist we get ValueError
4. l.append(element) -- add an element to list
5. l.insert(index, element) -- to add an element at the specified index
            If the index we specify is greater than max index it will get added to last
            We can pass negative index as well to the insert method
6. list1.extend(list2) -- add all the elements in list2 to list1.
            We can pass any sequence to extend method
7. l.remove(element) -- the specified element will be removed
        If the element doesn't exist it returns ValueError
8. l.pop() -- to remove and return the last element in the list
        If we run pop on empty list we get IndexError: pop from empty list
9. l.pop(index) -- removed the element at the specified index
        If we specify incorrect index we get -- IndexError: pop index out of range
10. l.reverse() -- to reverse the elements in the list       
11. l.sort() -- to sort the elements in list
        l.sort(reverse = True) -- to sort in descending order
        If we want to apply sort method the list should contain homogenous elements
12. l.copy() -- to create a copy of the list object
13. l.clear() -- to clear all the elements in the list     
        
'''

list1 = [10, 20, 30, 40, 50, 10, 10, 10, 30]
print(f'The number of elements in list {list1} is {len(list1)}')
print(f'The number of times the element 10 is present in the list {list1} is {list1.count(10)}')
print(f'The number of times the element 90 is present in the list {list1} is {list1.count(90)}')
print(f'The element 30 is present in the list {list1} at index {list1.index(30)}')

try:
    print(f'The element 90 is present in the list {list1} at index {list1.index(90)}')
except ValueError:
    print(f"The element 90 doesn't exist in the list {list1}")

list1.append(100)
print(f'list1 after adding element 100 is: {list1}')

list1.insert(3, 150)
print(f'list1 after adding element 150 at index 3 is: {list1}')

list1.insert(50, 1000)  # here 1000 will get added at last position
print(f'list1 = {list1}')

list2 = ['Ram',' Robert', 'Rahim']
list1.extend(list2)
print(f'list1 after extending elements of list2: {list1}')

list1.remove('Ram')
print(f'list1 after removing element Ram is: {list1}')

try:
    list1.remove('Sita')
except ValueError:
    print(f"Sita doesn't exist in the list {list1}")

print(f'Removing the last element in list: {list1.pop()}')
print(f'list1 after pop:- {list1}')

print(f'Popping the 4th element in the list1: {list1.pop(3)}')
print(f'list1 after second pop:- {list1}')

list1.reverse()  # Remember list is mutable all this methods won't return a new list object
print(f'list1 after calling reverse method: {list1}')

list2 = [98, 76, 45, 12, 90, 65]
list2.sort()
print(f'list2 after sorting: {list2}')

list2.sort(reverse=True)  # sorting in descending order
print(f'list2 after sorting in reverse order: {list2}')

x = [10, 20, 30, 40]
y = x  # This is called aliasing
y[1] = 777  # changes to variable y will get reflected to x because list is mutable
print(f'id(x) = {id(x)} and id(y) = {id(y)}')
print(f'x = {x}')

# If we want to create a copy of the list object we can use slice operator or copy method

x = [10, 20, 30, 40]
y = x.copy()
y[1] = 777  # x won't get changed here
print(f'id(x) = {id(x)} and id(y) = {id(y)}')
print(f'x = {x}')
print(f'y = {y}')

print(f'+ operator on lists: {x + y}')

list1.clear()
print(f'list1 after calling clear method is: {list1}')

print(f'Printing the values in nested list')
list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=' ')
    print()

# List Comprehensions
# Let's say if we want to create a list with the squares of first 10 numbers

# We will usually write code like this and do it

list1 = []
for x in range(1,11):
    list1.append(x * x)
print(list1)

# With the help of list comprehension we can easily do it

list1 = [x * x for x in range(1,11)]  # the length of the code will reduce drastically
print(list1)

list1 = [x + x for x in range(1,11)]  # we can perform any type of operation we want
print(list1)

list1 = [x * x for x in range(1,21) if x % 2 == 0]  # we can have if condition like this in list comprehension
print(list1)

words = ['Bat', 'Not', 'At', 'Cat']
first_char = [x[0] for x in words]  # extracting first character of every word in list
print(''.join(first_char))

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
list3 = [x for x in list1 if x not in list2]
print(list3)

sentence = "the quick brown fox jumps over lazy dog"
words = sentence.split()
content = [(w.title(),len(w)) for w in words]
print(content)

# Program to print all the vowels present in a sentence

vowels = 'aeiou'
vowels_list = []

for x in sentence:
    if x in vowels:
        if x not in vowels_list:
            vowels_list.append(x)

vowels_list.sort()
print(''.join(vowels_list))

# Lists cannot be used as keys in a dictionary
