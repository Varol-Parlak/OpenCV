import matplotlib.pyplot as plt 
import numpy as np
from sklearn.ensemble import IsolationForest
data = np.random.normal(scale=0.5, size=1000)

data = data.reshape(-1,1)

clt = IsolationForest(contamination=0.1)

pred = clt.fit_predict(data)

anomaly = np.where(pred == -1)[0]



plt.scatter(range(len(data)), data)
plt.scatter(anomaly, data[anomaly], c="r")

plt.show()