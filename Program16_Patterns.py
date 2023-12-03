"""
The below program explains some patterns using loops
"""

print('First pattern')

for i in range(1, 11):
    for j in range(i):
        print('*', end=' ')
    print()

print('Second pattern')

for i in range(1, 5):
    for j in range(i):
        print('* ' * i)

print('Third pattern')

for i in range(5, 0, -1):
    print('* ' * i)

