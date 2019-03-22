################################################################################
################################################################################
########################### ESTO ES PROVISIONAL ################################
################################################################################
################################################################################

import pandas as pd
import numpy as np

df = pd.read_excel('data.xlsx')
df_fechas = pd.read_csv('C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/01. 26Dic18 - Metas PowerBI/Enero2019/_Forecast/GoalsForecastsAndProbabilites/datesUpdate.csv')

month = list(df_fechas['month'])[0]
year = list(df_fechas['year'])[0]

df = df[(df['Mes'] == month) & (df['Año'] == year)]

print(df.shape)
print(df.head())