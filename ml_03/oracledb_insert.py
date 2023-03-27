import pandas as pd
import oracledb

conn = oracledb.connect(user='jsp4', password='123456', dsn='localhost:1521/doremiplay')
curs = conn.cursor()

sql = '''
INSERT INTO TEST (ID, NAME, CLASS_ID) VALUES ( (SELECT NVL(MAX(ID),0) +100), :2, :3)
'''
curs.execute(sql, ('800', '전진', 8))

print(curs.rowcount)

curs.close()
conn.commit()
conn.close()
