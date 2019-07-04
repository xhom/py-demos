# coding=UTF-8

import pymysql
pymysql.install_as_MySQLdb() # 用pymysql替代MySQLdb

# 1.连接数据库
# 打开数据库连接
db = pymysql.connect("localhost", "test", "123456", "test",charset='utf8')
#db = pymysql.connect("localhost", "test", "123456", "test", 3306,charset='utf8')
# 获取游标
cursor = db.cursor()
#执行sql
cursor.execute("SELECT VERSION()")
#获取一条数据
data = cursor.fetchone()
print "database version is %s"%(data)

# 2.创建数据库表
cursor.execute("DROP TABLE IF EXISTS tt")
sql1 = """CREATE TABLE tt (
         first_name  CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1),
         income FLOAT )"""

cursor.execute(sql1)

# 3.数据库插入操作
sql2 = """INSERT INTO tt(first_name,last_name, age, sex, income) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
sql3 = "INSERT INTO tt(first_name,last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s )"%('Jean', 'Lucy', 18, 'W', 5000)
def getSQL(index):
    return "INSERT INTO tt(first_name,last_name, age, sex, income) VALUES ('Mac"+str(index)+"', 'Mohan', "+str(20+i)+", 'M', 2000)"
try:
    #cursor.execute(sql2)
    for i in range(0,10):
        cursor.execute(getSQL(i))
    db.commit() #提交
    print '数据写入成功'
except Exception,e:
    db.rollback() #回滚
    print '数据写入失败,已回滚',e

# 4.数据库查询 fetchone/fetchall都会导致游标移动， 类似于java的 resultSet.next()
def selectAll():
    print '-----------------------------------------------------'
    cursor.execute("SELECT * FROM tt")
    item = cursor.fetchone()
    print 'fetchone: ',item
    print '影响行数：', cursor.rowcount # 只读
    rows = cursor.fetchall()
    print '数据查询结果：'
    for row in rows:
        print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" %(row[0], row[1], row[2], row[3], row[4] )
    print '-----------------------------------------------------'
selectAll()

# 5.更新数据库
sql4 =  "UPDATE tt SET age = age * 10 WHERE sex = 'M'"
try:
    cursor.execute(sql4)
    db.commit()
    print "更新数据成功"
except:
    db.rollback()
    print "更新数据失败"
selectAll()

# 6.删除数据
sql5 = "DELETE FROM tt WHERE age > 250"
try:
    cursor.execute(sql5)
    db.commit()
    print "删除数据成功"
except:
    db.rollback()
    print "删除数据失败"
selectAll()

# 关闭游标&数据库
cursor.close()
db.close()


# 执行事物 事务应该具有4个属性：原子性(atomicity)、一致性(consistency)、隔离性(isolation)、持久性(durability)。这四个属性通常称为ACID特性。
# commit rollback

# 错误处理， 有一些数据库相关的异常类，略