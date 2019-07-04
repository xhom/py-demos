# coding=UTF-8

# 1.异常处理
# except 相当于 catch
try:
    fh = open("modules/fh.txt", "r")
    int('xyz')
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError,err:
    print "没有找到文件或读取文件失败, error: ",err
except ValueError, err:
    print "不能转换为数字，error: ", err
else:
    print "内容写入文件成功"
    fh.close()
finally:
    print "不管有没有异常，我总会被执行！"

# 2.抛异常
# raise 相当于 throw
def functionName( level ):
    if level < 1:
        raise Exception("my exception: ", level)
        # 触发异常后，后面的代码就不会再执行

try:
    functionName(0)
except Exception,err:
    print err

# 3.自定义异常类 异常应该是典型的继承自Exception类，通过直接或间接的方式
class MyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise MyError('my error')
except MyError,err:
    print err.args

# 4.处理任何异常
try:
    functionName(0)
except:
    print '总之发生了异常，我不管是什么异常'

# 5.异常合并处理
try:
    fh = open("modules/fh.txt", "r")
    int('xyz')
    fh.write("这是一个测试文件，用于测试异常!!")
except (IOError,ValueError):
    print "IOError/ValueError 发生 了..."