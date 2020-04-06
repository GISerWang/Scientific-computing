# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
# 需要pip install PyMySQL
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:root, 数据库：test
conn = pymysql.connect(user='root', passwd='root', db='test', charset="utf8")
# 查询语句，选出public.tableName表中的所有数据
sql = "select * from public.tableName"
df = pd.read_sql(sql, con=conn)
print(df)