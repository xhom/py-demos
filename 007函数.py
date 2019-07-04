# coding=UTF-8

# 1.函数的定义
def print_me(list, msg="hello"):
    for item in list:
        print '正在打印' + item['name'] + '，版本号：'+ item['version']
    print msg
    print '打印完毕！'
    return

print_me([
    {'name':'item1','version':'1.0.0'},
    {'name':'item2','version':'1.0.1'},
    {'name':'item3','version':'1.0.2'},
])

def invoke_orint_me(f):
    list = [
        {'name':'item4','version':'1.0.4'},
        {'name':'item5','version':'1.0.5'},
        {'name':'item6','version':'1.0.6'}, # 最后的","也是正确的。和js一致
    ]
    f and f(list, "HELLO")
    return
# 事实证明，和js一样，函数也可以作为参数
invoke_orint_me(print_me)
# 2.lambda函数定义
sum = lambda arg1,arg2: arg1 + arg2
print 'sum=' + str(sum(100, 10))

global_var = "Im global var" # 全局变量
def test():
    inner_var = 'Im inner var' # 局部变量
    print 'test:', global_var
    print 'test:', inner_var
test()