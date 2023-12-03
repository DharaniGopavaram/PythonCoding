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



