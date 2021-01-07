import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = threadId
        self.delay = delay
        self.counter = counter

    def run(self):
        print('Starting thread: ' + self.name)
        while self.counter > 0:
            time.sleep(self.delay)
            print('%s: %s' % (self.name, time.ctime(time.time())))
            self.counter -= 1
        print('Finishing thread: ' + self.name)

thread1 = MyThread(1, 'Thread 1', 1, 5)
thread2 = MyThread(2, 'Thread 2', 1, 5)
thread1.run()
thread2.run()