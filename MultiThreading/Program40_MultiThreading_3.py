from threading import *
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

