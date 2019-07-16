# coding=UTF-8

import urllib # 爬虫库
import urllib2 # 爬虫库2
import cookielib #提供可存储cookie的对象，以便于与urllib2配合使用来访问Internet资源

def request(url, headers={}, params={}, cookieSetting=None, method='post'):
    cookie = None
    if(cookieSetting):
        savePath,loadPath = cookieSetting['savePath'],cookieSetting['loadPath']
        if savePath:
            cookie = cookielib.MozillaCookieJar(savePath)
        else:
            cookie = cookielib.MozillaCookieJar()
        if loadPath:
            cookie.load(loadPath, ignore_discard=True, ignore_expires=True)
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        cookie_opener = urllib2.build_opener(cookie_handler)

    req = None
    data = urllib.urlencode(params)
    if method.lower() == 'get':
        url = url + '?' + data
        req = urllib2.Request(url, headers=headers)
    else:
        req = urllib2.Request(url, data, headers)

    try:
        resp = None
        if(cookieSetting):
            resp = cookie_opener.open(req)
            cookieSetting['savePath'] and cookie.save(ignore_discard=True, ignore_expires=True)
        else:
            resp = urllib2.urlopen(req)
        return resp.read().decode("utf-8")
    except urllib2.URLError,e:
        print "请求失败I：", e.reason
    except urllib2.HTTPError,e:
        print "请求失败II：", e.code, e.reason
    return

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': 'https://www.baidu.com/' # 对付”反盗链”
}
params = {
    "username":'user',
    "password":'123456'
}
#print request("https://www.baidu.com",headers,params)