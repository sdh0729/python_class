import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv('time/2.2kw_L-EF-04_rotational imbalance.csv', delimiter=',', low_memory=False)

xts = data['z_axis']

gr_xts = xts[:500]

modelx = ARIMA(gr_xts, order=(2,0,3))

model_fitx = modelx.fit()

print(model_fitx.summary())

start_index = xts.index[0]
end_index = xts.index[500]


forecastx = model_fitx.predict(start=start_index, end=end_index, typ='levels')

plt.figure(figsize=(22,8))
plt.plot(forecastx,label = "predicted z")
plt.plot(gr_xts, label = 'original z')
plt.title("TS Forecast rotational imbalance z_axis")
plt.legend()
plt.show()
