import sqlite3 as sql
import pandas as pd
db = sql.connect(r'C:/Users/gxmlfx/Desktop/Debug/test.db')  # 连接数据库
c = db.cursor()  # 建立浮标
print("数据库打开成功")
cursor = c.execute("SELECT * FROM info")  # 读取数据库info表里所有数据
# cursor = c.execute("PRAGMA table_info(Faces)")
# print cursor.fetchall()
data = cursor.fetchall()  # 抓取c里的所有数据，list格式
# for row in data:
#     print(row[0])
# db.close()
# print (data)

df = pd.read_sql("SELECT * FROM info", con=db)  # 使用pandas直接读取数据库info表里所有数据，DataFrame格式
# print('数据形状\n',df.shape)
# print('数据类型\n',df.dtypes)
# print('----------')
# df.head()
