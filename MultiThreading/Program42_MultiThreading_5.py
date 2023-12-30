from threading import *
import time


def testing():
    print('child thread',current_thread().ident)
    time.sleep(3)
    print('thread name',current_thread().name,'completed')


# ident variable can be used to know the identification number of the thread
print('The main thread identification number is:',current_thread().ident)  # for every thread there is a number
# active_count() will give us the number of active threads
print('The number of active threads initially',active_count())
t1 = Thread(target=testing,name='testingThread-1')  # setting the name of the thread while creating the thread itself
t2 = Thread(target=testing,name='testingThread-2')
t3 = Thread(target=testing,name='testingThread-3')
t4 = Thread(target=testing,name='testingThread-4')
t1.start()
t2.start()
t3.start()
t4.start()
print('The child thread identification number is:',t1.ident)  # We can ident instance variable to get this

# is_alive is used to check whether the thread is alive or not
print('Checking whether the thread is alive or not',t1.is_alive())
print('The number of active threads after starting all the threads',active_count())

all_threads = enumerate()  # returns the thread objects of all the threads that are active
for t in all_threads:
    print('Thread name',t.name)
    print('Thread name',t.ident)

time.sleep(10)
print('The number of active threads after all the threads got completed',active_count())
print('Checking whether the thread is alive or not',t4.is_alive())

