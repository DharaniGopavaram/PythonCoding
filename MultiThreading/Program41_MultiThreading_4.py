from threading import *
import time


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

