# coding=UTF-8

import re
from demo003 import request

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
content = request("http://www.qiushibaike.com/hot/page/1", headers=headers)

pattern = re.compile(r'<div class="content">.*?</div>', re.S)
items = re.findall(pattern,content)
i = 1
pp = re.compile(r'<span>.*</span>', re.S)
for item in items:
    print i,": "
    print re.sub('(</*span>)|\s|<br/>','',pp.findall(item)[0])
    i += 1


p = re.compile(r'<img.*?>', re.S)
its = re.findall(p,content)
j = 1
print '\n=========================页面中所有的图片链接================================='
for it in its:
    print j,": "
    it = re.sub('(<img.*?src=")|(".*?>)','',it)
    it = re.sub('//','http://',it)
    if not re.match(r'http://',it):
        it = "http://www.qiushibaike.com"+it
    print it
    j += 1


pp = re.compile(r'<a.*?href.*?>', re.S)
itss = re.findall(pp,content)
k = 1
print '\n=========================页面中所有的链接====================================='
ppp = re.compile(r'href=".*?"', re.S)
for it in itss:
    it = ppp.findall(it)[0]
    it = re.sub('(href=")|"', '', it)
    if not re.match(r'(javascript)|#',it):
        print k, ": ",it
        k += 1