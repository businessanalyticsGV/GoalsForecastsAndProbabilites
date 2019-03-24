################################################################################
################################################################################
########################### ESTO ES PROVISIONAL ################################
################################################################################
################################################################################

#### I.- EXTRACTION AND TRANSFORMATION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
pd.set_option('display.max_columns',500)
pd.set_option('display.max_rows',500)

df = pd.read_excel('data.xlsx')
df_fechas = pd.read_csv('C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/01. 26Dic18 - Metas PowerBI/Enero2019/_Forecast/GoalsForecastsAndProbabilites/datesUpdate.csv')

month = list(df_fechas['month'])[0]
year = list(df_fechas['year'])[0]

df = df[(df['Mes'] == month) & (df['Año'] == year)].reset_index()

### ADDING FAKE PHOTOS
df['day'] = [int(date[:2]) for date in df['PhotoDate']]
df = df.sort_values(by=['day'])

for i in range(1,max(df['day'])):
    true = df[df['day'] == i].empty
    j = i
    while true:
        frame = df[df['day'] == i - 1]
        frame['day'] = j
        frame['PhotoDate'] = [str(j)+'-'+d[3:] if j > 9 else \
                              str(0)+str(j)+'-'+d[3:] for d in frame['PhotoDate']]

        frame['weekday'] = [datetime.datetime(int('20'+str(int(d[7:]))),
                                              int(d[4:5]),
                                              int(d[:2])).weekday() for d in frame['PhotoDate']]
        ## CONCAT AND SORT
        df = pd.concat([df,frame])
        df = df.sort_values(by='day')
        ## VERIFYING TRUE
        j = j + 1
        true = df[df['day'] == j].empty

### ADDING WEEKDAY

### ONEHOT CODING WEEKDAYS
for day in np.unique(df['weekday']):
    df['weekday_'+str(day)] = np.where(df['weekday'] == day,1,0)

df = df[[c for c in df if c.startswith('weekday_') or c in ['dia']]+['target']]
df = df.reset_index()
plt.plot(df['target'])
plt.show()

##### II.- TRAINING MODEL
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score,mean_squared_error
from scipy import stats


df.to_csv('Occupancy_forecast.csv', index = False)
print(df.shape)
print(df)
