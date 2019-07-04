# coding=UTF-8

# 1.循环控制语句
# break, continue, pass: pass是空语句，是为了保持程序结构的完整性

# 2.while循环
print "-------------------------while循环"
# while...else语法
count = 0
while count < 9:
    print 'The current count is ', count
    count += 1  # python不支持 n++
else:
    print 'count end with ', count
print "while execute end."

# 2.for循环
print "-------------------------for循环"
# 2.1 for...in 针对[]是item，针对{}是key
# 字符串循环
for letter in 'Python':
   print '当前字母 :', letter
# list循环
list = ['banana', 'apple', 'mango']
for item in list:
   print 'list:当前水果 :', item
# tuple循环
tuple = ('BANANA', 'APPLE', 'MANGO')
for item in tuple:
   print 'tuple:当前水果 :', item
# 字典循环
dict = {"a":'a-BANANA', 'b':'b-APPLE', "c":'c-MANGO'}
for key in dict:
   print 'dict:当前水果 :', key, ':',dict[key]
# 2.2 按index遍历
listSize = range(len(list))  # 内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。
for index in listSize:
    print 'list:当前水果 :', index, ":", list[index]
# 2.3 for...else
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。

# 3.嵌套循环
# 就是while+while, for+for, while+for的嵌套使用，没什么特别的

# 4.pass关键字 （break和continue和其他语言一样，这里略过）
# pass 是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。
print "-------------------------pass关键字"
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母 :', letter