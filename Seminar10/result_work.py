# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd
import random

def my_get_dummies(df):
    df_ret = pd.DataFrame(df)
    column_name = df_ret.columns[0]
    for name_columns in set(df_ret[column_name]):
        df_ret[name_columns] = False
        df_ret.loc[(df_ret[column_name] == name_columns), [name_columns]] = True
    df_ret.pop(column_name)
    return df_ret


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

#1 исходный data frame
df = pd.DataFrame({'whoAmI': lst})
print(df)

#2 встроенное преобразование к one hot
df2 = pd.get_dummies(df['whoAmI'])
print(df2)

#3 возможное преобразование к one hot
df3 = my_get_dummies(df['whoAmI'])
print(df3)
