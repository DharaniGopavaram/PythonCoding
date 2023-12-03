"""
The below program explains about dict data structure
If our data is in the form of key, value pairs then we should use dict data structure
In dict the keys can not contain duplicates whereas values can contain duplicates
dict is represented using curly braces only
"""

d = {100: 'dharani', 200: 'ravi', 300: 'shiva', 'roll-no': 1}
print(f'The type of the variable d is {type(d)} and it\'s value is {d}')
d[400] = 'john'
print(f'The values in d after adding element is {d}')
d[100] = 'Bunny'  # The value for key 100 gets overridden here
print(f'The value in d after modifying an element is {d}')

d1 = {}  # If we have just empty curly brace open and close it is by default dict only
print(f'The type of variable d1 is: {type(d1)}')

d1 = dict()  # We can create empty dictionary using dict function as well
print(f'The type of variable d1 created using dict method is: {type(d1)}')

d1[100] = 'Dharani'
d1[200] = 'Ram'
d1[300] = 'Shiva'
d1['Ramayana'] = 'Mahabharata'
print(f'The elements in the variables d1 after adding elements is: {d1}')
print(f'Accessing elements of a dictionary using key: {d1[100]}')

try:
    print(f'Accessing elements of a dictionary using key for key 400: {d1[400]}')
except KeyError:
    print(f"The key 400 doesn't exist in the dictionary {d1}")

for x in d1:  # by default x will contain only keys
    print(f"{x} -> {d1[x]}")

d1[200] = 'Sita'  # updating the value of Key 200

print(f'The values in dictionary d after updating Key 200 is:')
for x in d1:
    print(f"{x} -> {d1[x]}")

print(f'dictionary before deleting a key:{d1}')
del d1[100]  # deleting a key
print(f'dictionary after deleting a key:{d1}')

try:
    del d1[500]  # if the key doesn't exist we get KeyError
except KeyError:
    print(f"The key 500 doesn't exist in {d1}")

d1.clear()  # to delete all the elements
print(f'dictionary after calling clear method: {d1}')

list1 = [10, 20, 30]
d = {100: list1, 200: {'Dharani', 10, 20, 30}}  # we can have multiple values for a key
print(f'dictionary where key contains multiple values: {d}')

d = dict([(100, 'dharani'), (200, 'Ravi'), (300, 'Shiva')])  # we can pass tuple of tuples or set of tuples as well
print(f'dictionary created from list of tuples: {d}')
print(f'The length of the dictionary is: {len(d)}')

print(f'The value of the Key 100 using get method is: {d.get(100)}')
print(f'The value of the Key 500 using get method is: {d.get(500)}')  # this returns None since key doesn't exist
print(f'The value of the Key 500 using get method is: {d.get(500, "Not found")}')  # we can pass default value as well

print(f'Remove and return the value associated with the key: {d.pop(100)}')

try:
    print(f'Remove and return the value associated with the key: {d.pop(1000)}')
except KeyError:
    print(f"The key 1000 doesn't exist")

print(f'Removing some random key-value pair from dictionary: {d.popitem()}')
print(f'Removing some random key-value pair from dictionary: {d.popitem()}')

# print(f'Removing some random key-value pair from dictionary: {d.popitem()}')
# KeyError: 'popitem(): dictionary is empty'

print(f'The values in dictionary are: {d}')

d = dict([(100, 'dharani'), (200, 'Ravi'), (300, 'Shiva')])
print(f'The keys in dictionary are: {d.keys()}')
print(f'The values in dictionary are: {d.values()}')

for k, v in d.items():
    print(f'{k} -> {v}')

d1 = d.copy()
print(f'The variable d1 created from copy method is: {d1}')

d.setdefault(400, 'Kavya')  # If the key doesn't exist adds the key to the dictionary
d.setdefault(100, 'Sunny')  # since key 100 is already present it doesn't override the old value
print(f'The dictionary d = {d}')

d1 = {'a': 'apple', 'b': 'banana'}
d.update(d1)  # To add multiple values to dictionary
print(f'The data in dictionary after update method: {d}')

d = {'Ravi': 100, 'Shiva': 98, 'Ram': 90}
dict_values_sum = sum(d.values())   # sum is an inbuilt function
print(f'The sum of values in dictionary d is: {dict_values_sum}')
# program to print the number of occurrences of every character present in the string

s = 'mississippi'
d = {}
for x in s:
    d[x] = d.get(x,0) + 1

for k,v in d.items():
    print(f'{k} is available {v} times')

for k,v in sorted(d.items()):  # sort based on keys
    print(f'{k} is available {v} times')

# program to print the number of occurrences of every vowel present in the string

s = 'The quick brown fox jumps over lazy dog'
vowels_present = set(s) & set('aeiou')
d = {}

for x in vowels_present:
    d[x] = s.count(x)

for k,v in d.items():
    print(f'{k} came {v} times')

# Dictionary comprehension

squares = {x: x * x for x in range(1,11,2)}
print(squares)

doubles = {x: 2 * x for x in range(1,11,2)}
print(doubles)