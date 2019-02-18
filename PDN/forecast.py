import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

daysInMonth = 29

df = pd.read_excel('data.xlsx')
df['target'] = np.cumsum(df['Producción'])

X = np.array([[i+1] for i in range(df.shape[0])])
model = Ridge(fit_intercept=True, alpha=0.0, random_state=0, normalize=True)
model.fit(X,df['target'])

X = np.array([[i+1] for i in range(daysInMonth)])

y_hat = list(model.predict(X))
y_hat = [y_hat[i] if i >= df.shape[0] else -1 for i in range(len(y_hat)) ]
plt.plot(df['target'], label = 'Real')
plt.scatter(range(len(y_hat)),y_hat,marker='.', label = 'Forecasted',c='Red')
plt.plot([4577213.3 for i in range(len(y_hat))], linestyle=':')
print(model.predict([[daysInMonth]]))
plt.show()



