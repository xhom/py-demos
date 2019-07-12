# coding=UTF-8

import urllib # 爬虫库
import urllib2 # 爬虫库2
import cookielib #提供可存储cookie的对象，以便于与urllib2配合使用来访问Internet资源

# http proxy
# 右到网站会检测某一段时间内某个IP的访问次数，如果访问次数过多，它会禁止你的访问。
# 所以你可以设置一些代理服务器来帮助你，每隔一段时间换一个代理来避免被禁用
# 设置代理服务器是方式如下：
proxy_server = {"http" : 'http://some-proxy.com:8080'}
proxy_handler = urllib2.ProxyHandler(proxy_server)
proxy_opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(proxy_opener)

# cookie配置
# CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
#cookie = cookielib.CookieJar() # 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.MozillaCookieJar('cookies/baidu_cookie.txt') # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
#cookie.load('cookies/baidu_cookie.txt', ignore_discard=True, ignore_expires=True) # 从文件中读取cookie内容到变量
cookie_handler = urllib2.HTTPCookieProcessor(cookie) # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
cookie_opener = urllib2.build_opener(cookie_handler) # 通过handler来构建opener



# 请求参数配置
url = "https://www.baidu.com"
#url = "https://passport.baidu.com/v2/api/?login"
#url = "https://passport.csdn.net/account/login"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': 'https://www.baidu.com/' #对付”反盗链”
    
    '''
    User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    application/json ： 在 JSON RPC 调用时使用
    application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
    在使用服务器提供的 RESTFUL 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
    
    '''
}
params = {
    "username":'user',
    "password":'123456'
}
data = urllib.urlencode(params) # 请求数据包装
request = urllib2.Request(url, data, headers) # 构造请求
try:
    #response = urllib2.urlopen(request) # 发送请求并返回

    response = cookie_opener.open(request) # 此处的open方法同urllib2的urlopen方法，也可以传入request
    print '----------------cookie info--------------------'
    for item in cookie:
        print 'name: ' + item.name
        print 'value: ' + item.value
    print '------------------------------------------------'
    # 保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

    content = response.read()  # 读取响应内容
    print content
except (urllib2.URLError,urllib2.HTTPError), e:
    if(isinstance(e, urllib2.HTTPError)):
        print "请求失败I：", e.code, e.reason
    else:
        print "请求失败II：", e.reason


