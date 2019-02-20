import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from scipy import stats
import matplotlib.pyplot as plt

daysInMonth = 28
target = 4577213.3
target = 10000000

df = pd.read_excel('data.xls')
df['target'] = np.cumsum(df['Monto'])

X = np.array([[i+1] for i in range(df.shape[0])])
model = LinearRegression()
model.fit(X,df['target'])

y_hat = np.array([[i+1] for i in range(df.shape[0]+1,daysInMonth+1)])
y_hat = list(model.predict(y_hat))
y_toShow = [i for i in df['target']]+y_hat

plt.plot(y_toShow)

predictedLastDay = model.predict([[daysInMonth]])[0]

# ls_predicted = model.predict([[i+1] for i in range(daysInMonth)])
# ls_predicted = np.std(ls_predicted)

ls_predicted = r2_score(model.predict(X),df['target'])**(.5)
print(ls_predicted)
probabilityOfReaching = (target-predictedLastDay)/ls_predicted
probabilityOfReaching = stats.norm.cdf(probabilityOfReaching)
plt.show()
print('Probability of reaching 100% minimun: '+str(round(probabilityOfReaching,4)*100)+'%')