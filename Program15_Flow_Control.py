"""
The below program explains about flow control statements

    1. Conditional statements -- if, elif, else
    2. Iterative statements -- for, while
    3. Transfer control statements -- continue, pass, break

"""

# The below code explains conditional statements

name = input("Enter your name : ")
if name == 'Dharani':
    print('Hello Dharani! Good morning')
elif name == 'Kavya':
    print('Hello Kavya! Good Morning')
else:
    print('Hello Guest Good Morning')
print('How are you')

# The below code explains about iterative statements
# for loop is used when we know the number of iterations in advance

s = 'Dharani Kumar Gopavaram'
total_char_count = 0
for x in s:
    print(f'The character present at {total_char_count} index is {x}')
    total_char_count += 1
print(f'The total characters in the string {s} are {total_char_count}')

# while loop is used when we don't know the number of iterations in advance

i = 0
while i < len(s):
    print(f'The character present at {i} index is {s[i]}')
    i += 1

name = input('Enter your name : ')
pwd = input('Enter your password : ')
while name != 'Dharani' or pwd != 'python':
    name = input('Enter your name : ')
    pwd = input('Enter your password : ')
print('Hello Dharani thanks for confirmation')

# Nested for loops

for i in range(4):
    for j in range(4):
        print("i = {}, j = {}".format(i, j))

# for loops with break

for i in range(10):
    if i == 4:
        continue  # continue will skip current iteration
    elif i == 6:
        break  # break will come out of the loop
    print('The value of i is : {}'.format(i))

# for loop with else
# The statements in else block will get executed if the break statement didn't get executed in the loop

for i in range(10):
    if i == 6:
        break  # if the break statement gets executed it doesn't go to else block
    print('i is {}'.format(i))
else:
    print('The break statement did not get executed')

# else means loop without break
# syntactically if we require a block in our python program that don't anything we can use pass keyword
