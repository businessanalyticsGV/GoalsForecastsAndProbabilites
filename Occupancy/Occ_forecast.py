### I.- EXTRATING FILES FROM JULITOOOOOOO

import os
import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt ## CONVERTING INTEGERS TO DATES
from datetime import timedelta as td

path = '//nvocorpfileshare/inventory management/FRANCISCO JARAMILLO/REPORTES/Diario-INNSIST vs MATRIX/Base/2019/Marzo/'
ls_files = [file for file in os.listdir(path) if file[-len('.xlsx'):] == '.xlsx']

df = pd.DataFrame()
df_prueba = pd.DataFrame()
for files in ls_files:

    days_to_add = -367

    frame = pd.read_excel(path+files)
    print(files+' ready...'+str(len(np.unique(frame['Fecha'])))+str(frame.shape))
    frame['Fecha1'] = [dt.fromordinal(int(date)) for date in frame['Fecha']]
    frame['Año'] = [(datetime.date(d.year,d.month,d.day)+td(days=days_to_add)).year+1900 for d in frame['Fecha1']]
    frame['Mes'] = [(datetime.date(d.year,d.month,d.day)+td(days=days_to_add)).month for d in frame['Fecha1']]
    frame['Dia'] = [(datetime.date(d.year,d.month,d.day)+td(days=days_to_add)).day for d in frame['Fecha1']]

    # df_prueba = pd.concat([df_prueba,frame])
    # frame.to_excel('prueba.xlsx', index = False)
    llave = ['Año','Mes']
    real = frame.groupby(llave, as_index = False)[['Real']].sum()
    usoc = frame.groupby(llave, as_index = False)[['UC']].sum()
    invt = frame.groupby(llave, as_index = False)[['Inv Real']].sum()

    frame = real.merge(usoc,how='left',on = llave)
    frame = frame.merge(invt,how='left',on = llave)
    frame['Occupancy'] = (frame['Real']-frame['UC'])/frame['Inv Real']
    # frame = frame[llave+['Occupancy']]
    date = files[-11:][:6]
    frame['PhotoDate'] = str(date[-2:])+'/'+str(date[:4][-2:])+'/20'+str(date[:2])
    
    df = pd.concat([df,frame])
    
df.to_excel('data.xlsx', index = False)
# df_prueba.to_excel('prueba.xlsx', index = False)