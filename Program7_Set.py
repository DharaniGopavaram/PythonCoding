"""
The below program explains about set data structure
If we want to represent group of values as a single entity which is mutable where
    1. Insertion order is not preserved
    2. Duplicated are not allowed
    3. Heterogeneous objects are allowed
then we should use set data structure
Sets are represented using curly braces
"""

s = {30, 20, 30, 10, 20, 30}  # even though we add duplicates they are not considered
print(f'The type of the variable s is {type(s)} and it\'s value is {s}')

# we can not access set elements using index
# print(s[0])  # TypeError: 'set' object is not subscriptable
# since the order is not preserved in sets indexing and slicing is not applicable

print(f'Accessing elements of a set using for loop')
for x in s:
    print(x)

s.add('dharani')  # adding an element to set
print(f'The values in variable s after adding element is: {s}')

s.remove(20)  # removing an element from set
print(f'The values in variable s after removing element is: {s}')

s1 = set()  # to create an empty set we should use set() function
print(f'The type of the variable s1 is: {type(s1)}')

s = set('dharani')  # we can use set method to create sets from existing collection
print(f's = {s}')

list1 = [10, 20, 30, 40, 10, 20, 30]
s = set(list1)  # creating set from list -- here duplicates are automatically ignored
print(f's = {s}')

print(f'set = {set(range(1,11,2))}')  # creating set from range collection


# Important methods of set

'''
1. len(set) -- to know the number of elements present in the set
2. s.add(element) -- to add an element to set
3. s.update(sequence) -- to add all the elements in the sequence to set 
4. s.copy() -- to create a copy of the entire set object
5. s.pop() -- to remove and return some random element from the set
6. s.remove(element) -- to remove the specified element from the set
        If the element we specify doesn't exist we get KeyError
7. s.discard(element) -- same like remove but doesn't throw any error if the element doesn't exist
8. s.clear() -- To remove all the elements from set
'''

s = set()
print(f'The type of the variable s is {type(s)} and the number of elements in it is: {len(s)}')
s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(f'The elements in set after adding elements: {s}')
list1 = [100, 200, 300, 400, 500]
s.update(list1)  # adding all the list elements to set
print(f'The elements in set after adding list elements is: {s}')

tuple1 = (-1, -2, -3, -4)
name = 'dharani'
s.update(tuple1, name, range(10))  # We can add elements of multiple sequences at the same time as well

print(f'The elements in set after adding elements from multiple sequences is: {s}')

s1 = s.copy()
print(f'The elements in s1 which got copied from variable s is: {s1}')

print(f'The element that got popped from set is: {s.pop()}')
print(f'The element that got popped from set is: {s.pop()}')
print(f'The elements in s after running pop is: {s}')

s.remove(10)
print(f'The set after removing element 10: {s}')

try:
    s.remove('dharani')  # we get KeyError here
except KeyError:
    print(f"The dharani element doesn't exist in set")

s.discard('dharani')
s.discard(100)
print(f'The set after running discard method = {s}')

s.clear()
print(f'The elements in set after calling clear method: {s}')


# Mathematical operations on set

'''
1. s1.union(s2) or s1 | s2 -- will combine all the elements both in s1 and s2
2. s1.intersection(s2) or s1 & s2 -- will return the common elements in both s1 and s2
3. s1.diff(s2) or s1 - s2 -- will return the elements present in s1 but not in s2
4. s1.symmetric_difference(s2) or s1 ^ s2 -- except common elements will return everything in both sets
'''

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(f's1.union(s2) = {s1.union(s2)}')
print(f's1 | s2 = {s1 | s2}')
print(f's1.intersection(s2) = {s1.intersection(s2)}')
print(f's1 & s2 = {s1 & s2}')
print(f's1.difference(s2) = {s1.difference(s2)}')
print(f's1 - s2 = {s1 - s2}')
print(f's1.symmetric_difference(s2) = {s1.symmetric_difference(s2)}')
print(f's1 ^ s2 = {s1 ^ s2}')

# set comprehension

s1 = {x * x for x in range(1,6)}
print(f'set comprehension example 1: {s1}')

# Program to print all the vowels present in a given sentence

sentence = 'the quick brown fox jumps over lazy dog'
sentence_set = set(sentence)
vowels = {'a', 'e', 'i', 'o', 'u'}
print(f'The vowels present in the given sentence are: {"".join(sorted(sentence_set.intersection(vowels)))}')

