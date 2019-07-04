# coding=UTF-8

# 1.Number
# 整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型(floating point real values)
# 复数(complex numbers) - 复数由实数部分和虚数部分构成
import math # cmath模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数
print '----------------------------Number'
print dir(math)
print math.sqrt(9)
print math.pow(2,10)

# 2.String
print '----------------------------String'
str1 = "hello world,"
str2 = 'hello python!'
print str1, str2
print str1[0], str2[1:5] # 字符串截取
print str1[:6]+' good' # 用+拼接字符串
print '\n\n\\n' # 转义，与其他语言相同
# 字符串格式化，类似C语言 printf
print "My name is %s and weight is %d kg"%('Zara', 58)
# 三引号字符串, 支持多行并保留格式
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print errHTML
# 字符串内建函数
print str1.capitalize()
print str1.count("ll", 0, len(str1))
print str1.upper()
print errHTML.lower()

# 3.List
# 类似于js的数组，一个索引对应一个值，值的类型不限
# 在截取时的区间为 [start, end) 和其他语言一致， 语法： list[start:end]
print '----------------------------List'
list = ['physics', 'chemistry', 1997, 2000]
print list[0:2]
# 反向截取，从右到左，-1开始
print list[-2:]
# append追加元素 类似js arr.push()
list.append("append element")
print list
# del 删除列表元素
del list[3]
print list
# "+","*"在列表中使用,和字符串一致
new_list = list + ["new list",'list',1997] #相同的item并不会覆盖，正常现象，没什么奇怪
print new_list
double_list = list * 2
print double_list
#列表函数
print len(list)
print max(list)
print min(list)
list.reverse()
print list

# 4.Tuple （略，和List一致，只是元组不允许修改）

# 5.Dictionary
# 类似于Map这种数据结构
# 语法就是 JSON
# 可以按照js对象去理解
print '----------------------------Dictionary'
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict
del dict['Name']  # 删除键是'Name'的条目
print dict
print dict.keys()
print dict.values()
print dict.items()
dict.clear()      # 清空字典所有条目
print dict
del dict          # 删除字典
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住， 类似于js中key的覆盖
# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
# 注意 字典不能 obj.xxx 访问属性，只能 obj["xxx"]

# 6.日期和时间
print '----------------------------日期和时间'
import time, calendar
print "当前时间戳为:", time.time()
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
# 格式化,类似于数据库的格式化方法
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# 日历
cal = calendar.month(2019, 7)
print "以下输出2019年7月份的日历:"
print cal