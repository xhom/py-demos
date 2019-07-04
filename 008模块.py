# coding=UTF-8

# 1.整个模块引入 类似于js中 import support from 'modules'
from modules import support # 如果support在同目录下： import support

support.print_func('Python')
support.introduce({"name": "Jack", 'age':20})

# 2.单独引入模块中的函数， 类似于js中 import { print_func } from 'modules/support'
from modules.support import print_func
print_func('Java')

# 3.引入模块内部的所有
from modules.support2 import *
f1()
f2()

# 注意：如果引入的模块在别的路径下，需要在目录下存放__init__.py文件，才能被识别为包
from modules.tt.support3 import *
f3()