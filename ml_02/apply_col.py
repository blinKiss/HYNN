import numpy as np
import pandas as pd

# price = [
#     [25000, 30000, 15000],
#     [10000, 15000, 20000],
#     [50000, 30000, 70000]
# ]

# prod_price = pd.DataFrame(price)
# prod_price = prod_price.T

# label_name = ['Keyboard', 'Mouse', 'Storage']

# prod_price.columns = label_name
# print(prod_price)

prod_price = {
    'Keyboard' : [25000, 30000, 15000],
    'Mouse' : [10000, 15000, 20000],
    'Storage' : [50000, 30000, 70000]
}

prod_df = pd.DataFrame(
    prod_price
)

# 함수 prod_sale = 10% 할인가격으로 변환
def prod_sale(price) : 
    rst = price * 0.9
    return rst

# print(prod_sale(10000))

df_k = prod_df[['Keyboard', 'Mouse']].apply(prod_sale)
# print(df_k)
# df_k.rename(columns={'Keyboard' : 'Keyboard_Sale', 'Mouse' : 'Mouse_Sale'}, inplace=True)
df_k.columns = ['Keyboard_Sales', 'Mouse_Sales']
prod_df = pd.concat([prod_df, df_k], axis=1)
# print(prod_df)

# 모든 컬럼에 적용해서 K_sale, M_sale, S_sale 추가하시오
temp_s = pd.DataFrame()
temp_s['Storage_Sale'] = prod_df['Storage'].apply(prod_sale)
prod_df = pd.concat([prod_df, temp_s], axis=1)
print(prod_df)



