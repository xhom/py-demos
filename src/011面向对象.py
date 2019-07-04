# coding=UTF-8

# 1.类定义
class Employee:
    '所有员工的基类'
    empCount = 0 #数据成员
    #构造函数 名字固定“__init__”, self固定，相当于this，但是self并不是关键字
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(s):
        print '数量为：%d'%(s.empCount)
    def displayEmployee(this):
        print '姓名：',this.name,'薪水：',this.salary,"元"
    #所有方法 的第一个参数必须为必填，并且它是self
    def all(self):
        print self.__dict__
        print self.__doc__

    def __del__(self): # 析构函数，在对象被销毁时调用
        class_name = self.__class__.__name__
        print class_name, "销毁"

# 2.类实例化（创建对象）
zhangSan = Employee("张三", 2000)
liSi = Employee("李四",5000)

zhangSan.displayEmployee()
liSi.displayEmployee()
print '一共创建了%d个员工'%(Employee.empCount)

zhangSan.age = 7  # 添加一个 'age' 属性
zhangSan.age = 8  # 修改 'age' 属性
del zhangSan.age  # 删除 'age' 属性

hasattr(liSi, 'age')    # 如果存在 'age' 属性返回 True。
setattr(liSi, 'age', 8) # 添加属性 'age' 值为 8
getattr(liSi, 'age')    # 返回 'age' 属性的值
liSi.all()
delattr(liSi, 'age')    # 删除属性 'age'
print liSi.name

# 3.对象销毁（垃圾回收）
del zhangSan
del liSi

# 4.继承
class Parent:  # 定义父类
    parentAttr = 100
    __secretCount = 0  # 私有变量 private
    _protectCount = 0 # protected
    publicCount = 0  # 公开变量 public

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent,Employee):  # 定义子类
    'Child的文档'
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'

    # 方法重写Override
    def getAttr(self):
        print "父类属性（override） :", Child.parentAttr

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值
c.all()

#子类检测
print 'Child是Parent的子类吗？', issubclass(Child,Parent)
#实例检测
print 'c是Child的实例吗？',isinstance(c,Child)

# 重载也是支持的 Overload