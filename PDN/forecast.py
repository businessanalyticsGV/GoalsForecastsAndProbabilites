#### 0.- PRELIMINARIES

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from scipy import stats
import matplotlib.pyplot as plt
from datetime import datetime

#### I.- TRAINING MODEL
df = pd.read_excel('data.xlsx')
df['Fechaa'] = pd.to_datetime(df['Fechaa'], format = '%d/%m/%Y')
df['target'] = np.cumsum(df['Producción'])
df = df[['Fechaa','target']]

lr = LinearRegression()
X = [[i+1] for i in range(df.shape[0])]
lr.fit(X,df['target'])

#### II.- POWER BI DATA SET INCLUDING BOTH REAL AND PREDICTED VALUES
daysInMonth = 28
month = 2
year = 2019
target = 4577213.3

frame = pd.DataFrame()
dates = pd.date_range(start='01/'+str(month)+'/'+str(year),
                        end=str(daysInMonth)+'/'+str(month)+'/'+str(year))
dates = [date for date in dates]
frame['Fechaa'] = dates
frame['month'] = [d.month for d in frame['Fechaa']]
frame = frame[frame['month'] == month]
frame = frame.drop(columns = ['month'], axis = 1)
frame = frame.merge(df, how = 'left', on = ['Fechaa'])
frame['target'] = np.where(pd.isnull(frame['target']),np.nan,frame['target'])
frame['predicted'] = lr.predict([[i+1] for i in range(frame.shape[0])])
frame['to_powerbi'] = np.where(frame['target'] > 0,frame['target'],frame['predicted'])

#### III.- FINAL SCORE AND STORING FRAME
r2 = r2_score(df['target'],lr.predict([[i+1] for i in range(df.shape[0])]))

print(r2)
print(frame)