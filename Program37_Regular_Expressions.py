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
    3. match() -- will check whether the given pattern is present at the beginning of the string or not
        It returns match object if match is there otherwise returns None
    4. fullmatch() -- The pattern we specify should match the entire string
    5. search() -- search for the pattern in the entire string if no match return None
    6. findall() -- returns a list of all the matches
    7. sub() -- substitution or replacement -- re.sub(regex,replacement,target_string)
    8. subn() -- will return the substituted string along with the number of occurrences replaced
    9. split()

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
{n} -- exactly match for n occurrences
{m,n} -- minimum m number and maximum n number

^a -- whether the given string starting with a or not
a$ -- whether the string ends with a or not

"""

import re
import urllib.request

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
matcher = re.finditer(r'\s', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer(r'\S', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer(r'\w', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer(r'\W', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer(r'\d', 'a7 b@k9z A')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('.', 'a7 b@k9z A')  # . matches for every character
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a+', 'abaabcccaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a*', 'abaabcccaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a?', 'abaabcccaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a{3}', 'abaabcccaaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('a{2,3}', 'abaabcccaaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('^a', 'abaabcccaaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('b$', 'abaabcccaaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print()
matcher = re.finditer('z$', 'abaabcccaaaaab')
for match in matcher:
    print(f'The pattern {match.group()} is starting at index {match.start()} '
          f'and ending at {match.end() - 1}')

print('match function')
s = '[a-z]b+'
m = re.match(s,'abcdefg')
if m is not None:
    print(f'match is available on the given string and the start index is {m.start()}'
          f' and the pattern matched is {m.group()}')
else:
    print('The specified pattern is not at the beginning of the string')

s = '[a-z]{7}'
m = re.fullmatch(s,'abcdefg')  # the pattern we pass should match the complete string otherwise this returns None
if m is not None:
    print(f'fullmatch is available on the given string and the start index is {m.start()}'
          f' and the pattern matched is {m.group()}')
else:
    print('The specified pattern is not matching the entire string')

s = '[c-e]*f$'
m = re.search(s,'abcdefhhhf')  # search for pattern at any part of the string returns first occurrence
if m is not None:
    print(f'search is available on the given string and the start index is {m.start()}'
          f' and the pattern matched is {m.group()}')
else:
    print('The specified pattern doesn\'t exist at any part of the string')

s = '[c-e]*f'
m = re.findall(s,'abcdefhhhf')  # returns a list with all the matches
print(m)  # ['cdef', 'f']

print(re.findall(r'\W','a&&#13413*&ba'))  # this pattern will return the special characters
print(re.sub(r'\d','@','a4j7f9a8'))  # replace all the digits with @
print(re.subn(r'\d','@','a8ur5493184u'))  # ('a@ur@@@@@@@u', 8)
print(re.split(r'-','10-20-30-40'))  # split string based on a separator
print(re.split(r'\.','www.durgasoftvideos.com'))  # since . will match every character we need to escape it
print(re.split(r' +','dhaaa            kumar'))
print(re.search(r'EAsy$','Python is very easy'))  # None
print(re.search(r'EAsy$','Python is very easy',re.IGNORECASE).group())  # easy -- here we are ignoring case

'''
Write a program which will check whether the given string has the below characters or not
    1. The allowed characters are alphabets, digits and #
    2. first character should be lower case alphabet symbol from a to k
    3. second character should be any digit divisible by 3
    4. The length of identifier should be at-least two
'''

s = 'a6R#'
print(re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s).group())

print(re.fullmatch(r'[6-9]\d{9}','6748913719').group())  # Re to match 10 digit mobile numbers

# Reading and writing the matched regular expression data from and to a file

with open('dharani.txt','r') as f:
    with open('phone_number.txt','w') as f1:
        for line in f:
            match_list = re.findall(r'\b[6-9]\d{9}\b',line)  # some magic is there with r
            for match in match_list:
                f1.write(match + '\n')

# web scrapping using regular expressions
sites = ['http://example.com/','http://google.com/']

for site in sites:
    print('Searching...',site)
    u = urllib.request.urlopen(site)
    text = u.read()
    title = re.findall("<title>.*</title>",str(text),re.IGNORECASE)
    print(title)

# regular expression to match email ids

print(re.fullmatch(r'\w[a-zA-Z0-9.-]+@(gmail|yahoo)[.](com|net)','dharani.gopavaram@gmail.com'))
print(re.fullmatch(r'\w[a-zA-Z0-9.-]+@(gmail|yahoo)[.](com|net)','dharani.gopavaram@yahoo.net'))
print(re.fullmatch(r'\w[a-zA-Z0-9.-]+@(gmail|yahoo)[.](com|net)','12345@yahoo.net'))
print(re.fullmatch(r'\w[a-zA-Z0-9.-]+@(gmail|yahoo)[.](com|net)','?12345@yahoo.net'))  # this doesn't match

