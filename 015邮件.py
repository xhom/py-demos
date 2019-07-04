# coding=UTF-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendMail(sender, receivers, msg):
    charset = msg['charset']

    message = MIMEText(msg['content'], msg['format'], charset)
    message['From'] = Header('sender', charset)
    message['To'] = Header('receiver', charset)
    message["Subject"] = Header(msg['subject'], charset)

    try:
        server = smtplib.SMTP()
        server.connect(sender['host'], sender['port'])
        server.login(sender['user'], sender['pass'])
        server.sendmail(sender['user'], receivers, message.as_string())

        server.quit() # 关闭连接
        print '邮件发送成功'
    except smtplib.SMTPException, e:
        print '无法发送邮件', e

sender = {
    'host': "smtp.189.cn", # 邮件服务器地址
    'port': 25, # 端口号
    'user': "x_hom@189.cn", # 用户
    'pass': "zgDX@189" # 口令
}
receivers = ['xhom@foxmail.com'] # 邮件接收地址
msg1 = {
    "format": "plain", # 邮件格式
    "charset": "utf-8", # 编码
    "subject": "测试文本邮件", # 邮件主题
    "content": "python测试邮件内容..." # 邮件内容
}
msg2 = {
    "subject": "测试HTML邮件", # 邮件主题
    "format": "html", # 邮件格式
    "charset": "utf-8", # 编码
    "content": """
        <h3>这是 python 发送的 html 邮件</h3>
        <p><a href="http://www.baidu.com">百度一哈</a></p>
        """
}

#sendMail(sender, receivers, msg1)
sendMail(sender, receivers, msg2)

#还可以发送带 附件的邮件 和 带html中含资源文件的邮件 略