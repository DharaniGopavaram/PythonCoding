"""
The below program explains about frozenset data structure.
frozenset is same like set the only difference is frozenset is immutable whereas set is mutable
"""

s = {10, 20, 30, 40, 'dharani', 1}
fs = frozenset(s)
print(f'The type of the variable fs is {type(fs)} and it\'s value is {fs}')

# We can not add or remove elements from frozenset
# fs.add(50)  # AttributeError: 'frozenset' object has no attribute 'add'
