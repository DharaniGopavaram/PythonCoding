"""
The below program explains about strings and slice operator.
String is a sequence of characters
Slice operator is used to extract substring from the original string.

In Python Strings will have two indexes.

+ve index -- from left to right
-ve index -- from right to left

"""

s = 'dharani kumar gopavaram'
print(f'Accessing value at index 0 from the string {s} which is {s[0]}')
print(f'Accessing value at index 3 from the string {s} which is {s[3]}')
print(f'Accessing last element of the string {s} using negative index which is {s[-1]}')

# If we try to access index which doesn't exist we get IndexError
# print(f'Trying to access index which does not exist: {s[10]}') # IndexError: string index out of range

# printing the positive and negative index of every character in a string

positive_index = 0
for c in s:
    print(f'The character at +ve index {positive_index} and -ve index {positive_index - len(s)} is {c}')
    positive_index += 1

# String methods

'''
len -- to know the length of the string i.e number of characters

lstrip -- remove the left side spaces of the string
rstrip -- remove the right side spaces of the string
strip -- remove both left and right side spaces of the string

The lstrip, rstrip and strip methods doesn't remove in between spaces

Methods to know the position of the substring -- find, rfind, index, rindex

find -- to know the position of substring in the original string.
        If the substring is not available it will return -1
rfind -- same like find but will search for substring in the reverse direction

The find method is overloaded it has two forms
find(substring) -- will search for the substring from beginning to the end of the string
find(substring,begin) -- will search from the begin index we specify to the end of the string
find(substring,begin,end) -- will search for the substring between the begin and end - 1 we specify

index method is same like find method the only difference is 
If the substring is not available index method returns ValueError

s.count(substring) -- to know the number of occurrences of the passed substring in the given string
s.count(substring, begin) -- will return the count starting from begin index
s.count(substring, being, end) -- will search for the substring from begin to end - 1 index

s.replace(old_string, new_string)
s.replace(old_string, new_string, count) -- count will tell how many times we need to old_string with new_string

s.split(separator) -- default separator is space -- returns a list of strings
s.split(separator, count) -- count indicates how many times you want to perform the split
s.rsplit(separator, count) - same like split but will do the splitting in the reverse direction

separator.join(l) -- to create a string out of a collection

s.upper() -- To convert all the characters to uppercase
s.lower() -- To convert all the characters to lowercase
s.swapcase() -- convert uppercase to lowercase and vice-versa
s.title() -- first character of every word in the string starts with uppercase
s.capitalize() -- first character of the string starts with uppercase rest all the characters are lowercase

s.startswith(substring) -- To know whether our string is starting with a particular substring or not
s.endswith(substring) -- To know whether our string is ending with a particular substring or not

isalnum() -- check whether the string contains only alphanumeric characters or not(a-z, A-Z, 0 to 9)
isalpha() -- checks whether the string contains only alphabet characters or not
isdigit() -- checks whether the string contains only digits or not
islower() -- checks whether the string contains only lower alphabet symbols or not
isupper() -- checks whether the string contains only upper alphabet symbols or not
istitle() -- checks whether the string contains words in title case or not
isspace() -- checks whether the string contains only space or not

sorted(s) -- sort the characters in the string and returns list
chr(int) -- will return the character present in the ASCII value we passed
ord(character) -- will return the ASCII value of the character we passed

'''

print(f'The number of characters present in the string is: {len(s)}')

s = '   Dharani Kumar Gopavaram    '
print(f"s.lstrip() = {s.lstrip()}")
print(f"s.rstrip() = {s.rstrip()}")
print(f"s.strip() = {s.strip()}")

s = 'durgasoftdurgasoft'

print(f"s.find('soft') = {s.find('soft')}")
print(f"s.find('soft', 6) = {s.find('soft', 6)}")
print(f"s.find('soft', 5, 8) = {s.find('soft', 5, 8)}")  # this will return -1

try:
    print(f"s.index('soft', 5, 9) = {s.index('soft', 5, 9)}")
    print(f"s.index('z') = {s.index('z')}")
except ValueError:  # If there is an exception it will get handled here
    print(f"The substring you are searching is not present")
else:  # this block will get executed if the code didn't reach except block
    print(f"The substring you are searching is present")

# Program to display all the occurrences of a substring in the given string

substring = 'soft'
pos = -1
occur = 0

while True:
    pos = s.find(substring, pos + 1)
    if pos == -1:
        break
    print(f'The substring {substring} is present at index: {pos}')
    occur += 1

if occur == 0:
    print('The substring you are searching is not found')

print(f'The number of times the {substring} is present in {s} is {s.count(substring)}')
print(f'The number of times the {substring} is present in {s} from index 5 to end is {s.count(substring, 5)}')
print(f'The number of times the {substring} is present in {s} between index 5 and 10 is {s.count(substring, 5, 10)}')

print(f"s.replace('a', 'z') = {s.replace('a', 'z')}")
print(f"s.replace('soft', 'software') = {s.replace('soft', 'software')}")
print(f"s.replace('soft', 'software') = {s.replace('soft', 'software', 1)}")  # Replace only the first occurrence

s = 'dharani Kumar Gopavaram'
print(f'Original String = {s}')
print(f's.split() = {s.split()}')  # returns a list
print(f's.lower() = {s.lower()}')
print(f's.upper() = {s.upper()}')
print(f's.swapcase() = {s.swapcase()}')
print(f's.title() = {s.title()}')
print(f's.capitalize() = {s.capitalize()}')

s = 'Dharani123Kumar'
print(f'Original string: {s}')
print(f's.isalnum() = {s.isalnum()}')
print(f's.isalpha() = {s.isalpha()}')
print(f's.islower() = {s.islower()}')
print(f's.isupper() = {s.isupper()}')
print(f's.istitle() = {s.istitle()}')

s = 'Dharani,Kumar,Gopavaram'
print(f'Original String = {s}')
print(f's.split(",") = {s.split(",")}')  # ['Dharani', 'Kumar', 'Gopavaram']
print(f's.split(",", 1) = {s.split(",", 1)}')  # ['Dharani', 'Kumar,Gopavaram']
print(f's.rsplit(",", 1) = {s.rsplit(",", 1)}')  # ['Dharani,Kumar', 'Gopavaram']

print(f's.startswith("dharani") = {s.startswith("Dharani")}')
print(f's.endswith("dharani") = {s.endswith("Gopavaram")}')

list1 = ["Dharani", "Kumar", "Gopavaram"]
print(f'list1: {list1}')
print(f'Creating a string out of list1 using join method: {"".join(list1)}')
print(f'Creating a string out of list1 using join method: {" ".join(list1)}')
print(f'Creating a string out of list1 using join method: {",".join(list1)}')

'''
slice operator syntax :-

s[begin:end:step] 

step value can be either positive or negative

If the step value is positive it is always going consider from left to right from begin to end - 1
In forward direction the default value of begin is 0 and the default value of end is length of the string

If the step value is negative it is always going consider from right to left from begin to end + 1
In backward direction the default value of begin is -1 and the default value of end is -(length of string + 1)
If the end in the reverse direction is -1 the result is always empty string
'''

s = '0123456789'
print(f'The original string is s = {s}')
print(f's[1:5] = {s[1:5]}')  # will return all the characters starting from index 1 to 4
print(f's[:4] = {s[:4]}')  # will return all the characters starting from index 0 to 3
print(f's[2:] = {s[2:]}')  # will return all the characters starting from index 2 till end of the string
print(f's[:] = {s[:]}')  # will return a copy of the original string
print(f's[-1:-4] = {s[-1:-4]}')  # since we can not go from -1 to -4 from left to right we get empty string
print(f's[-4:-1] = {s[-4:-1]}')  # will return all the characters from -4 to -2 index
print(f's[100:] = {s[100:]}')  # slice operator won't give any index out of range error it will return empty string
print(f's[1:7:2] = {s[1:7:2]}')  # will return every second character starting from index 1 to 6

print(f's[::-1] = {s[::-1]}')  # will print the string in reverse order
print(f's[2:8:-1] = {s[2:8:-1]}')  # will print empty string since we can not go from right to left from 2 to 9
print(f's[8:2:-1] = {s[8:2:-1]}')  # 876543
print(f's[-1:-6:-1] = {s[-1:-6:-1]}')  # 98765
print(f's[2:-5:1] = {s[2:-5:1]}')  # 234
print(f's[1:6:-2] = {s[1:6:-2]}')  # empty string
print(f's[0:-5:-5] = {s[0:-5:-5]}')  # empty string
print(f's[:0:-1] = {s[:0:-1]}')  # 987654321
print(f's[-1::-1] = {s[-1::-1]}')  # 9876543210
print(f's[-5:0:-9] = {s[-5:0:-9]}')  # 5
print(f's[2:-1:-1] = {s[2:-1:-1]} ')  # empty string because the end will become 0 after adding +1

# Program to print the string in reverse order

s = 'dharani kumar gopavaram'

# 1st way using slice operator

print(f'The reverse of the string {s} is:{s[::-1]}')

# 2nd way to use the reversed function

reversed_s = reversed(s)
print(f'The reverse of the string {s} is:', end='')
for x in reversed_s:
    print(x,end='')
print()

# using reversed with join method

print(f'The reverse of the string {s} is:{"".join(reversed(s))}')

# 3rd way by writing the code

i = len(s) - 1
print(f'The reverse of the string {s} is:', end='')
while i >= 0:
    print(s[i],end='')
    i -= 1
print()

# Program 2
# input :- Dharani Kumar Gopavaram
# output :- Gopavaram Kumar Dharani

s = 'Durga Software Solutions'
print(f"Reversed of only the words in the string {s} is:{' '.join(reversed(s.split()))}")

# Program 3
# input :- Durga Software Solutions
# output :- agruD erawtfoS snoituloS

print(' '.join([x[::-1] for x in s.split()]))

# Program 4 -- Print the characters at even position and at odd position

# using slice operator
s = 'durga software solutions'
print(f'Characters at even position: {s[::2]}')
print(f'Characters at odd position: {s[1::2]}')

# without using slice operator
index = 0
even_char = ''
odd_char = ''

while index < len(s):
    even_char += s[index]
    if index + 1 < len(s):
        odd_char += s[index+1]
    index += 2

print(f'The characters at even position: {even_char}')
print(f'The characters at odd position: {odd_char}')

# Program 5
# input :- B4A1D3
# output :- ABD134

s = 'B4A1D3'
chars = digits = ''

for x in s:
    if x.isdigit():
        digits += x
    else:
        chars += x

# sorted function can be used to sort strings and it will return list

sorted_chars, sorted_digits = ''.join(sorted(chars)), ''.join(sorted(digits))
print(f'The input is: {s}')
print(f'The output is: {sorted_chars + sorted_digits}')

# Program 6
# input :- a20b3
# output :- aaaaaaaaaaaaaaaaaaaabbb

s = 'A20B3C50'

found_char = found_digit = output = output1 = ''

for x in s:
    if x.isalpha():
        if not found_char:
            found_char = x
        else:
            output += found_char * int(found_digit)
            output1 += found_char + chr(ord(found_char) + int(found_digit))
            found_char = x
            found_digit = ''
    else:
        found_digit += x

output += found_char * int(found_digit)
output1 += found_char + chr(ord(found_char) + int(found_digit))

print(f'The input is: {s}')
print(f'The output is: {output}')
print(f'The output1 is: {output1}')

# Program 6
# input :- s1 = 'RAVI', 'RAMAKRISHNA'
# output :- RRAAVMIAKRISHNA

s1 = 'RAMAKRISHNA'
s2 = 'RAVI'
output = ''
max_length = max(len(s1), len(s2))
i = 0

while i < max_length:
    if i < len(s1):
        output += s1[i]
    if i < len(s2):
        output += s2[i]
    i += 1

print(f'The output is: {output}')

# Program 7
# Remove duplicate characters from the string

s = 'aaaaabbbb'
output = ''

print(f'The original string is: {s}')

# using set
print(f"The string without duplicates is: {''.join(set(s))}")  # order will be lost

# by writing the code
for x in s:
    if x not in output:
        output += x

print(f'The string without duplicates is: {output}')


# Print the number of occurrences of every character in the string

s = 'aaaaabbbb'
d = {}

for x in s:
    if x not in d.keys():  # keys method will return only the keys present in the dictionary
        d[x] = 1
    else:
        d[x] += 1

print(f'The number of occurrences of every character in the string is: ')
for k,v in d.items():  # items method will return both key and value
    print(f'{k} -> {v}')
