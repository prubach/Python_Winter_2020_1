import threading
import time
import multiprocessing

class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay, counter, shared_list):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = threadId
        self.delay = delay
        self.counter = counter
        self.shared_list = shared_list

    def run(self):
        print('Starting thread: ' + self.name)
        while self.counter > 0:
            time.sleep(self.delay)
            print('%s: %s' % (self.name, time.ctime(time.time())))
            shared_list.append(self.name + ': ' + str(self.counter))
            self.counter -= 1
        print('Finishing thread: ' + self.name)

print('CPUs: %s' % (multiprocessing.cpu_count()))

shared_list = []
thread1 = MyThread(1, 'Thread 1', 1, 5, shared_list)
thread2 = MyThread(2, 'Thread 2', 1, 5, shared_list)
thread3 = MyThread(3, 'Thread 3', 1, 5, shared_list)
thread1.start()
thread2.start()
thread3.start()
all_threads = []
all_threads.append(thread1)
all_threads.append(thread2)
all_threads.append(thread3)
for thr in all_threads:
    thr.join()

print(shared_list)

print('Exiting Main Thread')