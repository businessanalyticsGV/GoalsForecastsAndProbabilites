import pandas as pd
import numpy as np

df = pd.read_excel('data.xlsx')
df['target'] = np.cumsum(df['Producción'])

