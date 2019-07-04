# coding=UTF-8

# 1.函数式线程创建
import thread
import time

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print "%s: %s"%(threadName,time.ctime(time.time()))

try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 4))
except:
    print '启动线程错误'

while 1:
   pass