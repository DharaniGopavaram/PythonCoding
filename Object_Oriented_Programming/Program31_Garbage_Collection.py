"""
Garbage collection(GC)
In Python, Programmer is responsible to create object and GC will take care of destroying the object
GC will remove unwanted/useless objects from memory
If object doesn't have any reference variable then it is eligible for GC.

We have a module called gc to customize gc in our program

1. gc.isenabled() -- To know if gc is enabled or not
2. gc.disable() -- To disable garbage collection
3. gc.enable() -- To enable garbage collection

Destructors:- named with __del__
Garbage collector will call destructor before destroying the object to perform cleanup activities.

"""

import gc
import sys
print('Is garbage collection enabled:',gc.isenabled())
gc.disable()  # disabling the gc
print('Is garbage collection enabled:',gc.isenabled())
gc.enable()
print('Is garbage collection enabled:',gc.isenabled())


class Test:
    def __init__(self):
        print('Constructor execution')
        self.name = 'Dharani'

    def __del__(self):
        print('Destructor execution')


t = Test()
print(f'Number of references {sys.getrefcount(t)}')  # This will return 2 including the implicit self variable
t = None  # Once we assign to None the Test() object previously created id eligible for GC
# Before destroying the object
print('End of application')

l1 = [Test(),Test(),Test()]
del l1  # this will delete all the Test() objects created in l1
