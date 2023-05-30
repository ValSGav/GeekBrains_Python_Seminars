# 1. Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)
# Чтобы подключить датасет с
# пингвинами, воспользуйтесь данным
# скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('seminar10/sample_data/penguins.csv')
# print(df.describe())
# print(df.columns)

# sns.scatterplot(x='island', y='body_mass_g', data=df)
# plt.show()

# cols = ['species', 'island', 'bill_length_mm', 'bill_depth_mm',
#        'flipper_length_mm', 'body_mass_g', 'sex']
# g= sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# # plt.show()

# sns.scatterplot(x='island', y='body_mass_g', data=df, style=)
# # sns.heatmap(data=df.corr(numeric_only=True), cmap='coolwarm')
# plt.show()

# . Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ
#print(df.head)

df.loc[(df['flipper_length_mm'] < 180), ['height_group']] = 'low'
df.loc[(df['flipper_length_mm']> 180) % (df['flipper_length_mm'] < 190), ['height_group']] = 'mid'
df.loc[(df['flipper_length_mm'] > 190), ['height_group']] = 'high'

sns.histplot(data = df , x='flipper_length_mm', hue='height_group')
plt.show()