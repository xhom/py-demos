# coding=UTF-8

def computeResult(x, y, op):
    result = ""
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "%":
        result = x % y
    elif op == "**":
        result = x ** y
    elif op == "//":
        result = x // y
    elif op == "==":
        result = x == y
    elif op == "!=":
        result = x != y
    elif op == "<>":
        result = x <> y
    elif op == ">":
        result = x > y
    elif op == "<":
        result = x < y
    elif op == ">=":
        result = x >= y
    elif op == "<=":
        result = x <= y
    elif op == "and":
        result = x and y
    elif op == "or":
        result = x or y
    elif op == "not":
        result = not x
    elif op == "in":
        result = x in y
    elif op == "not in":
        result = x not in y
    else:
        result = ""
    print x, op, y, ": ", result
    return

print "--------------------------算术运算符"
# 1.算术运算符
a, b = 22, 7
computeResult(a, b, "+")
computeResult(a, b, "-")
computeResult(a, b, "*")
computeResult(a, b, "/")
computeResult(a, b, "%")
computeResult(a, b, "**")  # a的b次方
computeResult(a, b, "//")  # 取整除 - 返回商的整数部分（向下取整）

print "--------------------------比较运算符"
# 2.比较运算符
computeResult(a, b, "==")
computeResult(a, b, "!=")
computeResult(a, b, "<>")
computeResult(a, b, ">")
computeResult(a, b, "<")
computeResult(a, b, ">=")
computeResult(a, b, "<=")

# 3.赋值运算符
# =, +=, -+, *=, /=, %=, **=, //=

print "--------------------------逻辑运算符"
# 4.逻辑运算符, 类似js, and or短路后会返回一个值 ： a = a||0;
# and, or, not
computeResult(a, b, "and")
computeResult(a, b, "or")
computeResult(a, b, "not")

print "--------------------------成员运算符"
# 5.成员运算符
# in, not in 注意在字典中查找的是key并不是value
list = [1,22,7,"sss"]
tuple = (1,22,7,'sss')
dict = {"a": "AAA",'b': 22,}
dict2 = {"a": "AAA",22: "BBB",}
dict3 = {"a": "AAA","22": "BBB",}
computeResult(a, list, "in")
computeResult(a, list, "not in")
computeResult(a, tuple, "in")
computeResult(a, dict, "in")
computeResult(a, dict2, "in")
computeResult(a, dict3, "in")

# 6.身份运算符
# is, is not
# x is y 等价于：id(x) == id(y) 注：id()函数用于获取对象内存地址
# x is not y 等价于：id(x) != id(y)