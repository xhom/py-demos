# coding=UTF-8

import urllib
import urllib2 #扒网页的库，还有urllib可用

# urlopen(url, data, timeout)
# url:资源地址
# data:要传送的数据，默认为None
# timeout:超时时间（秒），默认值为socket._GLOBAL_DEFAULT_TIMEOUT
response = urllib2.urlopen('http://www.baidu.com')
content = response.read() #资源内容（网页的话就是html）
print content

# urlopen(urllib2.Request)
# 通过构造Request发送请求(更通用，可以在request里配置所有请求相关参数)
request = urllib2.Request("http://www.taobao.com")
response = urllib2.urlopen(request)
content = response.read()
print content

# POST/GET
# GET直接把参数放到url之后即可：?a=xxx&b=yyy
# 下面是post的方式
params = {"username":"user","password":"123456"}
data = urllib.urlencode(params) #请求数据包装
url = "https://passport.csdn.net/account/login"
try:
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    content = response.read()
    print content
except urllib2.HTTPError, e:
    print '请求失败',e
# GET： url = url + "?" + data