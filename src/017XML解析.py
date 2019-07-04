# coding=UTF-8

# Python 有三种方法解析XML: SAX，DOM，以及 ElementTree
# ElementTree: ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少

# 1.SAX
# SAX是一种基于事件驱动的 API
# 利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器
import xml.sax

class myXmlPraser(xml.sax.ContentHandler):
    def __init__(self):
        self.currTag = ""

        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
    def startElement(self, tag, attrs): # Override
        #print '-----------------start-',tag
        self.currTag = tag
        if tag == 'movie':
            print "=======Movie======="
            title = attrs['title']
            print '片名：', title
    def endElement(self, tag): # Override
        if self.currTag == 'type':
            print "类型：", self.type
        elif self.currTag == 'format':
            print "格式：", self.format
        elif self.currTag == 'year':
            print "年份：", self.year
        elif self.currTag == 'rating':
            print "评级：", self.rating
        elif self.currTag == 'stars':
            print "星星：", self.stars
        elif self.currTag == 'description':
            print "简介：", self.description
        self.currTag = ''
        #print '-------------------end-', tag
    def characters(self, content): # Override
        if self.currTag == "type":
            self.type = content
        elif self.currTag == "format":
            self.format = content
        elif self.currTag == "year":
            self.year = content
        elif self.currTag == "rating":
            self.rating = content
        elif self.currTag == "stars":
            self.stars = content
        elif self.currTag == "description":
            self.description = content

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = myXmlPraser()

    parser.setContentHandler(handler)

    parser.parse("../modules/movies.xml")

# 2.DOM - 适合转json用
import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree = xml.dom.minidom.parse("../modules/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
    print '根节点: ' + str(collection.getAttribute('shelf'))

movies = collection.getElementsByTagName('movie')

for movie in movies:
    print '=======Movie======='
    if movie.hasAttribute('title'):
        print '片名：' + str(movie.getAttribute('title'))
    type = movie.getElementsByTagName('type')[0]
    print '类型：' + str(type.childNodes[0].data)


# 3.