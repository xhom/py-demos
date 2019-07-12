# coding=UTF-8

# 正则
import re
from demo003 import request

#print request("https://www.baidu.com")

pattern = re.compile(r'hello') #注意hello前面的r的意思是“原生字符串”
'''
 • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
 • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
 • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
 • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
 • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
 • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

'''

def print_result(text, method='match', p=pattern):
    if method=='search':
        result = re.search(p, text)
        print_rest(result, text)
    elif method=='split':
        result = re.split(p, text)
        print_rest(result,text,True)
    elif method=='findall':
        result = re.findall(p, text)
        print_rest(result,text,True)
    else:
        result = re.match(p, text)
        print_rest(result, text)

def print_rest(result,text,f=False):
    if f:
        print result
    else:
        if result:
            ss = result.groups()
            print text, ': ', ss
        else:
            print text + ": 匹配失败"


print_result("hello python，hello java")
print '--------------------------------'
print_result("hello python，hello java", 'search')
print '--------------------------------'
print_result('one12two333three5four09', 'split', r'\d+')
print '--------------------------------'
print_result('one12two333three5four09', 'findall', r'\d+')
