import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from scipy import stats
import matplotlib.pyplot as plt

daysInMonth = 28
# target = 4201000.03
target = 3000000

df = pd.read_excel('data.xlsx')
df['target'] = np.cumsum(df['Producción'])

X = np.array([[i+1] for i in range(df.shape[0])])
model = Ridge(fit_intercept=True, alpha=0.0, random_state=0, normalize=True)
model.fit(X,df['target'])

y_hat = np.array([[i+1] for i in range(df.shape[0]+1,daysInMonth+1)])
y_hat = list(model.predict(y_hat))
y_toShow = [i for i in df['target']]+y_hat

plt.plot(y_toShow)

predictedLastDay = model.predict([[daysInMonth]])[0]

ls_predicted = model.predict([[i+1] for i in range(daysInMonth)])
ls_predicted = np.std(ls_predicted)

print(ls_predicted)
probabilityOfReaching = (target-predictedLastDay)/ls_predicted
probabilityOfReaching = stats.norm.cdf(probabilityOfReaching)

print(probabilityOfReaching)

print('Predicted last day: '+str(predictedLastDay))

# plt.show()