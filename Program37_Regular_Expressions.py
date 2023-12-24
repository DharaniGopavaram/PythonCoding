"""
The below program explains about regular expressions in Python
If we want to represent a group of strings according a particular pattern then we should go for regular expressions
The module we use for regular expressions in Python is re module.

re module contains several functions
    1. compile() function -- To create pattern object
    2. finditer() -- returns an iterator object with all the matches
        a. start() -- returns the starting index of the pattern
        b. end() -- returns the end + 1 index of the pattern
        c. group() -- returns the substring matched

[abc] -- Either a or b or c
[^abc] -- Except a or b or c
[a-z] -- all the lower case alphabets
[A-Z] -- any upper case lower case alphabets
[a-zA-Z] -- any alphabet symbol
[0-9] -- any digit
[a-zA-Z0-9] -- any alphanumeric
[^a-zA-Z0-9] -- other than alphanumeric characters like special characters

\s -- search for space character
\S -- except space character
\d -- for digits
\D -- except digits
\w -- [a-zA-Z0-9] only alphanumeric characters
\W -- [^a-zA-Z0-9] except alphanumeric characters everything like special characters

. -- matches any character

+ -- one or more
* -- zero or ore occurrences
? -- zero or one

"""

import re

pattern = re.compile('ab')  # To create a pattern we need to search use compile function
print(f'The type of the variable pattern is: {type(pattern)}')
matcher = pattern.finditer('abaababa')
count = 0
for match in matcher:
    print('match is available at start index:', match.start())
    count += 1
print('The number of occurrences:', count)

print('searching for pattern ba in the same string')
pattern = re.compile('ba')
matcher = pattern.finditer('abaababa')
for match in matcher:
    print(f'The pattern ba is starting at index {match.start()} '
          f'and ending at index {match.end() - 1} and the substring is {match.group()}')

print('simplified version of above two code snippets')
# Instead of creating a pattern object first we can use finditer method directly like below
matcher = re.finditer('ab', 'abaabab')  # finditer returns a callable_iterator object
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at index {match.end() - 1} ')

print()
matcher = re.finditer('[ab]', 'a7b@k9z')  # searching for either a or b in the string we passed
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[^ab]', 'a7b@k9z')  # searching for except a or b in the string we passed
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[a-z]', 'a7b@k9z')  # searching for all the lower case alphabets
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[^a-z]', 'a7b@k9z')  # searching except lower case alphabets
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[0-9]', 'a7b@k9z')  # searching only for digits
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[^0-9]', 'a7b@k9z')  # searching for everything except digits
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('[^a-zA-Z0-9]', 'a7b@k9z')  # searching only for special characters
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('\s', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('\S', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('\w', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('\W', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('\d', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('.', 'a7 b@k9z A')  # . matches for every character
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a+', 'abaabcccaaaab')  # . matches for every character
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a*', 'abaabcccaaaab')  # . matches for every character
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a?', 'abaabcccaaaab')  # . matches for every character
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')