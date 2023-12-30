from threading import *
import time


def job1():
    print('job1 execution')
    print(current_thread().name,'is daemon:',current_thread().daemon)
    t1 = Thread(target=job2,name='ChildThread2')
    t1.start()


def job2():
    print('job2 execution')
    print(current_thread().name,'is daemon:',current_thread().daemon)


t = Thread(target=job1,name='ChildThread1')
t.daemon = True  # Now all the threads this child thread initiates are by default daemon
t.start()
time.sleep(2)
print('End of main thread')


# After starting the thread we can't change the daemon nature of it
