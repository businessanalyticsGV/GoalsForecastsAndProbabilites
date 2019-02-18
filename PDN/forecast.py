import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
df['target'] = np.cumsum(df['Producción'])

X = np.array([[i+1] for i in range(df.shape[0])])
model = Ridge(fit_intercept=True, alpha=0.0, random_state=0, normalize=True)
model.fit(X,df['target'])

X = np.array([[i+1] for i in range(29)])
plt.plot(df['target'])
plt.plot(model.predict(X),linestyle=':')
plt.show()

