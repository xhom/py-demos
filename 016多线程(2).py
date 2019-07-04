# coding=UTF-8

# 2.对象式线程创建
import threading
import time

def print_time2(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self) # 相当于 super()
        self.name = name
        self.delay = delay
    def run(self): # run是override函数
        print "启动 " + self.name
        print_time2(self.name, self.delay, 5)
        print '结束 ' + self.name
th1 = myThread("线程-1", 1)
th2 = myThread("线程-2", 2)

th1.start()
th2.start()

print '主线程退出'
