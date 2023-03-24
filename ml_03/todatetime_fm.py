from datetime import datetime
import pandas as pd

test_df = pd.DataFrame({
    'order_dt' : ['01/03/20', '02/04/21', '03/05/22']

})


# 연도 2자리면 y 4자리면 Y
test_df['dttm_1'] = pd.to_datetime(test_df['order_dt'], format = '%d/%m/%y')
# print(test_df)

# strftime(' ') 
# - %a : 요일 출력, %A : 요일 출력(긴 이름), %w : 요일 출력(숫자, 0부터 일요일)
# - %d : 날짜 출력(2자리)
# - %b : 월 출력, %B : 월 출력(긴 이름), %m : 월 출력(숫자)
# - %y : 연 출력(2자리), %Y : 연 출력(4자리)
# - %H : 시간 출력(24시간), %I : 시간 출력(12시간)
# - %p : AM 또는 PM 출력
# - %M : 분 출력(2자리)
# - %S : 초 출력(2자리)
# - %f : 마이크로 초 출력

# 월을 글자로 출력
test_df['month'] = pd.to_datetime(test_df['order_dt'], format = '%d/%m/%y').dt.strftime('%B')
# print(test_df['month'])

today = datetime.now()
today2 = today.strftime('%Y-%b-%d')
# print(today2)

time = today.strftime('%H:%M:%S')
# print(time)

test_df['dttm_1'] # 시리즈 형태

for dttm in test_df['dttm_1']:
    print(dttm.strftime('%Y-%b-%m'))