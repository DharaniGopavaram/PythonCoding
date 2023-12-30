from threading import *
import time


def display():
    for i in range(10):
        print('Seetha thread')
        time.sleep(1)


t = Thread(target=display)
t.start()

# Main thread will enter into waiting state until child thread t gets completed
t.join(5)  # join() method will make the current thread wait until the thread where we specified join gets completed
# If we pass a parameter to join method it will wait for the number of seconds we specified
for i in range(10):
    print('Rama thread')
