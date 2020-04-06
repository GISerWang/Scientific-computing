# -*- coding: utf-8 -*-
import psycopg2
import pandas as pd
# 需要pip install psycopg2
# 初始化数据库连接，使用psycopg2模块
# PostgreSQL的用户：postgres, 密码:123456, 数据库：test
conn = psycopg2.connect(database='test', user='postgres', password='123456')
# 查询语句，选出public.tableName表中的所有数据
sql = "select * from public.tableName"
df = pd.read_sql(sql, con=conn)
print(df)