# coding=UTF-8

# 1.标识符，由字母、数字、下划线组成，但不能以数字开头大小写敏感
_foo = "_foo代表不能直接访问的类属性"
__foo = "__foo代表类的私有成员"
__foo__ = "__foo__代表 Python 里特殊方法专用的标识"
print _foo, __foo, __foo__

# 2.缩进
if True:
    print "True"
    print "1"
else:
    print "False"  # python是通过缩进来划分语句块的
    print "0"

# 3.多行语句
total = "hello-" + \
    "world-" + \
    "haha"
print total
days = ['Monday', 'Tuesday', 'Wednesday',  # 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
        'Thursday', 'Friday']
print days

# 4.python的引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 5.Python注释 python中单行注释采用 # 开头
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 6.console输入
# raw_input("按下 enter 键退出，其他任意键显示...\n")

# 7.print
print "不换行",
print "不换行X"
print "打印两遍" * 2
print "字符串" + "拼接"

# 8.变量 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print counter, miles, name
# Python允许你同时为多个变量赋值
a = b = c = 1 # 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
aa, bb, cc = 10, 20, "john"
print a, b, c, aa, bb, cc

# 9.python数据类型（五个标准的数据类型）
# Numbers（数字:10,12.33） String（字符串:'xxx',"xxx"） List（列表:[]） Tuple（元组:()） Dictionary（字典:{}）
del a, b, c # 变量删除
s = 'abcdefg'
print s[1:5] # 字符串截取
print s[5:]
print s[:5]
print s[0]
print s[1:6:2] # 2是步长
print s * 2
print s + 'ABCDEFG'
# List
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# Tuple 元组不能二次赋值，相当于只读列表
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# tuple[0] = "xxx"    TypeError: 'tuple' object does not support item assignment
# Dictionary 列表是有序的对象集合，字典是无序的对象集合
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two" # 2非下标，而是key，和js的对象有异曲同工之妙
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

# 10.Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可
# int(x [,base]), long(x [,base] ), float(x), str(x)