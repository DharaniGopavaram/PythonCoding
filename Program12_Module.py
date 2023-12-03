"""
The below program shows different ways of importing modules to our application
"""

import math
import os as o  # giving alias name to the imported module
from random import randint, choices  # This syntax will help us import the required functions present in the module

print(f'using sqrt function in math module math.sqrt(100) = {math.sqrt(100)}')
print(f'getting the pi value using math function math.pi = {math.pi}')
print(f"checking whether a file exists or not")
print(o.path.exists('/Users/dharani-kumar/Documents/Final_Interview_Preparation'))  # using alias name
print(f'Using randint function in random module directly: {randint(10, 100)}')  # directly using function
print(f'Using randint function in random module directly: {choices([10, 20, 30])}')


