# 192.168.0.156 학원
# 알아서 집
# 테스트계정 사용 userid, userpw
# TEST 테이블
import pandas as pd
import oracledb

conn = oracledb.connect(user='jsp4', password='123456', dsn='localhost:1521/doremiplay')
curs = conn.cursor()

sql = "SELECT COUNT(*) AS CNT FROM TEST"
curs.execute(sql)

out_data = curs.fetchone()
# print(out_data) # 몇개인지 체크

sql2 = "SELECT * FROM TEST"
curs.execute(sql2)

out_data2 = curs.fetchall()

df = pd.DataFrame(out_data2)
print(df)
