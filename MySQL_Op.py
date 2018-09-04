import pymysql

#链接数据库
db = pymysql.connect('127.0.0.1', \
	'root', '123456', charset='utf8')

#创建游标对象
cursor = db.cursor()

#创建数据库
#cursor.execute('create database test')

#选择数据库
cursor.execute('use test')

'''
#创建表格
sql_tb = """CREATE TABLE student (
         Name CHAR(20) NOT NULL,
         Sex char(20),
         Student_ID char(20)
          )"""
cursor.execute(sql_tb)
'''

#选择数据表
cursor.execute('select * from student')

#插入数据
def InsertTB(Name, Sex, student_ID):
	sql_Insert = "insert into student (Name, Sex, student_ID)\
	 values ('{}', '{}', '{}')".format(Name, Sex, student_ID)
	cursor.execute(sql_Insert)
	db.commit()

#删除数据
def DeleteTB():
	sql_Delete = "delete from student where Name = '阚保春'"
	cursor.execute(sql_Delete)
	db.commit()

#查看数据
def DisplayTB():
	sql_Display = "select * from student"
	cursor.execute(sql_Display)
	results = cursor.fetchall()
	db.commit()	
	print(results)


Name = '阚保春'
Sex = '男'
student_ID = '1109030311'
#InsertTB(Name, Sex, student_ID)
#DeleteTB()
DisplayTB()

