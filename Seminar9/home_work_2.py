#  Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('seminar9\california_housing_train.csv')

print(df.loc[(df.population < df.population.quantile(.05)), ['households']].max())