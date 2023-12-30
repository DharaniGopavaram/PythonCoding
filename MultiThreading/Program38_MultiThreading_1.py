"""
The below program explains about multi-threading in Python
Executing several tasks simultaneously is called multitasking.
In general in any programming language there are two types of multitasking.
    1. Process based multitasking -- Executing several tasks simultaneously where each task is an independent
        process
    2. Thread based multitasking -- Executing several tasks simultaneously where each part is a separate independent
        part of the same program is thread based multitasking and each independent part is called Thread.
        Thread based multitasking helps us to reduce execution time and improve performance

    By default, every python contains one thread which is called Main Thread.

There are 3 ways of creating thread in Python

1. Creating a thread without using any class
2. Creating a thread by extending Thread class
3. Creating a thread without extending Thread class

"""

from threading import *
import time

# creating a thread without using any class


def display():
    for i in range(10):
        print(f'This line is executed by: {current_thread().name} and the value of i is {i}')


print(current_thread().name)  # main thread execution
t = Thread(target=display)  # Main thread will create child thread
t.start()  # Once we come to this line a new child thread will get created, and it's job is to call display function
print(current_thread().name)  # this is again main thread execution only
for i in range(10):
    print(f'This is executed by Main thread and the value of i is {i}')