"""
The below program explains about tuple data structure

If we want to represent a group of values as a single entity which is immutable where

    1. insertion order is preserved
    2. duplicates are allowed
    3. heterogeneous objects are allowed (meaning different types of objects)

then we should use tuple data structure
Tuples are represented using parentheses
Read only version of list is tuple
"""

tuple1 = (10, 20, 30, 40)
print(f'The type of the variable tuple is {type(tuple1)} and it\'s value is {tuple1}')
print(f'Accessing first element of tuple using positive index: {tuple1[0]}')
print(f'Accessing last element of tuple using negative index: {tuple1[-1]}')
sliced_tuple1 = tuple1[1:3]
print(f'sliced tuple = {sliced_tuple1}')
print(f'Accessing elements of a tuple using for loop')

for x in tuple1:
    print(x)

# tuple1[0] = 100  # TypeError: 'tuple' object does not support item assignment
print(f'The repetition operator on tuple: {tuple1 * 2} ')

tuple1 = 10, 20, 30, 40, 50  # we are not required to pass the elements in parentheses for tuple
print(f'The type of the variable tuple is {type(tuple1)} and the values in it are: {tuple1}')

tuple1 = (10)  # This is not considered as a tuple instead it is int
print(f'The type of the variable tuple is {type(tuple1)} and the value is {tuple1}')

tuple1 = (10,)  # The syntax to represent one valued tuple
print(f'The type of the variable tuple is {type(tuple1)} and the value is {tuple1}')

tuple1 = ()  # To create an empty tuple just open and close the parentheses like this
print(f'The type of the variable tuple is {type(tuple1)} and the value is {tuple1}')

# tuple function can be used to convert other sequences to tuple
print(f"tuple('dharani') = {tuple('dharani')}")
print(f"tuple([10, 20, 30, 40]) = {tuple([10, 20, 30, 40])}")
print(f"tuple(range(1,11,2)) = {tuple(range(1, 11, 2))}")

# Important methods of tuple

'''
1. len(tuple1) -- to know the number of elements present in the list
2. t.count(element) -- to know the number of occurrences of specified substring in the given tuple
3. t.index(element) -- to know the first index of the specified element in the tuple
4. sorted(tuple) -- to sort the elements in the tuple
5. min(tuple) -- returns the minimum value element in the tuple
6. max(tuple) -- returns the maximum value element in the tuple
'''

tuple1 = (10, 20, 30, 40, 50, 10)
print(f'The number of elements present in the tuple {tuple1} is {len(tuple1)}')
print(f'The number of occurrences of element 10 present in the tuple {tuple1} is {tuple1.count(10)} ')

try:
    print(f'The element 10 is present at index {tuple1.index(10)} in the tuple {tuple1}')
    print(f'The element 100 is present at index {tuple1.index(100)} in the tuple {tuple1}')
except ValueError:
    print(f"The specified element doesn't exist in the tuple")

sorted_tuple1 = sorted(tuple1)  # sort method returns list
print(f'The sorted tuple = {sorted_tuple1}')

sorted_tuple1_desc = sorted(tuple1, reverse=True)
print(f'The sorted tuple in descending order = {sorted_tuple1_desc}')

print(f'The minimum value element in the tuple {tuple1} is {min(tuple1)}')
print(f'The maximum value element in the tuple {tuple1} is {max(tuple1)}')

# Tuple packing and tuple unpacking

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d  # This is called tuple packing
print(f'packing tuple = {t}')

p, q, r, s = t  # this is called tuple un-packing
print(p, q, r, s)

# We can apply this packing and un-packing on any type of sequence

# Tuple comprehension is not supported

t = (x * x for x in range(1,21))  # here the return type is generator
print(type(t))  # <class 'generator'>
for x in t:
    print(x,end=',')

# Tuples can be used as keys for dictionary
