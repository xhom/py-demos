# coding=UTF-8

# 1.控制台输出
print "Python 是一个非常棒的语言，不是吗？ emmm..."
print "%s是个挺好的语言吧" %("python")

# 2.键盘输入
str1 = raw_input('raw_input-请输入点啥：') # 从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
print '小子，你的输入是: '+ str1
str2 = input("input-请输入点啥：") # 和 raw_input函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回
print "小子，你的输入是: ", str2

# 3.文件打开/关闭
import time
foo = open('modules/foo.txt','r+') # 打开文件
# 文件常用属性
print '文件名：',foo.name
print '访问模式：',foo.mode
print '是否已关闭：',foo.closed
print '末尾是否强制加空格：',foo.softspace
# 文件写入
#foo.write("content be written ["+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"]\n")
# 文件读取
content = foo.read(10) # 10为制定字节数，不指定则读取全部文件内容
print '读取的内容是：', content
#文件定位
position = foo.tell()
print '当前位置：', position
#重命名
import os
#os.rename('modules/foo.txt','modules/foo2.txt')
# 删除一个已经存在的文件test2.txt
#os.remove("modules/foo2.txt")
# 创建目录
os.mkdir('modules/ttt')
# 删除目录
os.rmdir('modules/ttt')
# 改变当前目录
#os.chdir('xxx')
# 获取当前目录
print os.getcwd()

# 关闭打开的文件
foo.close()
# mode取值:
# r： 读，指针在开始
# r+: r+写
# w: 写，创建，覆盖，指针在开始
# w+: w+读
# a: 写，创建，指针在结尾
# a+: a+读

