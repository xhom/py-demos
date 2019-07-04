# coding=UTF-8

import re

print(re.match('www', 'www.xxx.com').span())  # 在起始位置匹配
print(re.match('com', 'www.xxx.com'))         # 不在起始位置匹配

# 不常用 略...