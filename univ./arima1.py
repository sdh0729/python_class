import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv('time/2.2kw_L-EF-04_rotational imbalance.csv', delimiter=',', low_memory=False)

xts = data['x_axis']
yts = data['y_axis']
zts = data['z_axis']
gr_xts = xts[:500]
gr_yts = yts[:500]
gr_zts = zts[:500]

modelx = ARIMA(gr_xts, order=(2,0,3))
modely = ARIMA(gr_yts, order=(2,0,3))
modelz = ARIMA(gr_zts, order=(2,0,3))
model_fitx = modelx.fit()
model_fity = modely.fit()
model_fitz = modelz.fit()

print(model_fitx.summary())
print(model_fity.summary())
print(model_fitz.summary())

start_index = xts.index[0]
end_index = xts.index[500]
start_indey = xts.index[0]
end_indey = xts.index[500]
start_indez = xts.index[0]
end_indez = xts.index[500]

forecastx = model_fitx.predict(start=start_index, end=end_index, typ='levels')
forecasty = model_fity.predict(start=start_indey, end=end_indey, typ='levels')
forecastz = model_fitz.predict(start=start_indez, end=end_indez, typ='levels')
plt.figure(figsize=(22,8))
plt.plot(forecastx,label = "predicted x")
plt.plot(forecasty,label = "predicted y")
plt.plot(forecastz,label = "predicted z")
plt.title("TS Forecast rotational imbalance")
plt.legend()
plt.show()
