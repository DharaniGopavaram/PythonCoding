from threading import *


# creating a thread by extending thread class -- this is recommended
class MyThread(Thread):
    def run(self):  # once we create a thread and start it the code in the run method will get started automatically
        for i in range(10):
            print(f'{current_thread().name} and the value of i is {i}')


t = MyThread()
t.start()
for i in range(20):
    print(f'This is again MainThread and the value of i is {i}')
