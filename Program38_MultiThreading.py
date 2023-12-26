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
    for i in range(100):
        print(f'This line is executed by: {current_thread().name} and the value of i is {i}')


print(current_thread().name)  # main thread execution
t = Thread(target=display)  # Main thread will create child thread
t.start()  # Once we come to this line a new child thread will get created, and it's job is to call display function
print(current_thread().name)  # this is again main thread execution only
for i in range(10):
    print(f'This is executed by Main thread and the value of i is {i}')


# creating a thread by extending thread class
class MyThread(Thread):
    def run(self):  # once we create a thread and start it the code in the run method will get started automatically
        for i in range(10):
            print(f'{current_thread().name} and the value of i is {i}')


t = MyThread()
t.start()
for i in range(20):
    print(f'This is again MainThread and the value of i is {i}')

# creating a thread without extending Thread class


class Test:
    @staticmethod
    def display():
        for i in range(10):
            print('child thread')


t = Thread(Test.display())
t.start()
for i in range(10):
    print('This is again main thread only')


def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('The double of the number is:',n * 2,'which was executed by the thread',current_thread().name)


def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('The square of the number is:',n * n,'which was executed by the thread',current_thread().name)


begin_time = time.time()
nums = [1,2,3,4,5,6,7,8,9,10]
t1 = Thread(target=doubles,args=(nums,))  # we can pass arguments to target method using args
t2 = Thread(target=squares,args=(nums,))
t1.name = 'double-thread'  # setting the name for the thread
t2.name = 'squares-thread'
t1.start()
t2.start()
t1.join()  # join method waits for both the threads to complete
t2.join()  # this is called thread synchronisation
end_time = time.time()
print('Total time took to execute the program is',end_time - begin_time)
