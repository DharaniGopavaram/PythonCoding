"""The below program explains about public and private variables in OOP
By default all the variables are public
If you want to make a variable private you should start the variable with __
"""


class Test:
    def __init__(self):
        self.__x = 10

    def __str__(self):
        return f'This is Test class with {self.__x} attribute'

    def display(self):  # private variables can only be accessed inside the class using a method
        print(f'The value of the private variable is:{self.__x}')


# This syntax will help us differentiate if we are calling the methods directly or indirectly
if __name__ == '__main__':
    t = Test()
    # print(t.__x)  # AttributeError: 'Test' object has no attribute '__x'
    t.display()
    print('Accessing private variable using special syntax:',t._Test__x)  # object_reference._ClassName__variable_name
    print(t)  # <__main__.Test object at 0x10136ae40>
    # If we want to print a meaningful result while printing the object
    # After implementing __str__ function the output will be what ever we defined
