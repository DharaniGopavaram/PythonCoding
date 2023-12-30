"""
The threads which are running in the background are called daemon threads.
The daemon threads provide support for the threads in our program.
Garbage collector is one of the daemon thread.
We can change the daemon nature of the child threads we start using t.setDaemon(True) but we should set it
    before starting the thread. We can not change the daemon nature of a thread after starting it.
It is impossible to change the daemon nature of the MainThread.
By default, for all the remaining threads the daemon nature will be inherited from parent.
If the last non-daemon thread terminates all the daemon threads will be terminated
"""

from threading import *
import time

print('The current running thread is daemon or not:',current_thread().daemon)
# current_thread().daemon = True  # RuntimeError: cannot set daemon status of active thread


def job():
    for i in range(10):
        print('Lazy thread')
        time.sleep(2)


# MainThread is the parent of this child thread since MainThread is non-daemon this child thread is also non-daemon
t = Thread(target=job)
print('Child thread is daemon',t.daemon)
t.daemon = True  # setting the child thread to daemon thread
t.start()
time.sleep(5)
print('MainThread completed')

# If the child thread is non-daemon even when the MainThread gets completed the child thread will keep continuing
# If the child thread is daemon once main thread gets completed the child thread will get stopped
