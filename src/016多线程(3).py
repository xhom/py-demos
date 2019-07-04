# coding=UTF-8

# 线程同步

import threading
import time

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print '线程启动：'+self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        threadLock.release() # 释放锁

threadLock = threading.Lock()

threads = []

th1 = myThread(1,'th1',1)
th2 = myThread(2,'th2',2)

th1.start()
th2.start()

threads.append(th1)
threads.append(th2)

for t in threads:
    t.join()

print '退出主线程'

# 线程优先级队列 略