import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from pandas import datetime

data = pd.read_csv('time/2.2kw_L-DEF-01_normal.csv', delimiter=',', low_memory=False)
data_ch = pd.read_csv('time/2.2kw_L-DSF-01_axis misalignment.csv', delimiter=',', low_memory=False)
data_ro = pd.read_csv('time/2.2kw_L-EF-04_rotational imbalance.csv', delimiter=',', low_memory=False)
data_ba = pd.read_csv('time/2.2kw_L-SF-04_bad bearing.csv', delimiter=',', low_memory=False)
data_be = pd.read_csv('time/2.2kw_R-SF-03_belt slack.csv', delimiter=',', low_memory=False)

zts = data_be['z_axis']
yts = data_be['y_axis']
xts = data_be['x_axis']

ts_ch = data_ch['z_axis']
ts_ro = data_ro['z_axis']
ts_ba = data_ba['z_axis']
ts_be = data_be['z_axis']
print(ts)

gr_zts = zts[:500]
gr_yts = yts[:500]
gr_xts = xts[:500]
gr_ts_ch = ts_ch[:500]
gr_ts_ro = ts_ro[:500]
gr_ts_ba = ts_ba[:500]
gr_ts_be = ts_be[:500]

train_ts = ts[:10000]
test_ts = ts[67667500:]
print(train_ts)
print(len(train_ts))
print(len(test_ts))

model = ARIMA(train_ts, order=(2,1,2))
model_fit = model.fit()
print(model_fit.summary())
start_index = datetime(67667500, 6, 25)
end_index = datetime(67667999, 5, 31)

print(start_index)

forecast = model_fit.predict(start=start_index, end=end_index, typ='levels')

plt.figure(figsize=(22,8))
plt.plot(weather_bin.Date,weather_bin.MeanTemp,label = "original")
plt.plot(forecast,label = "predicted")
plt.title("Time Series Forecast")
plt.xlabel("Date")
plt.ylabel("Mean Temperature")
plt.legend()
plt.show()
'''
''''
def Gr(DATA,COLOR,TITLE):
    plt.plot(DATA,color=COLOR)
    plt.title(TITLE)
    plt.show()
Gr(gr_ts,'b','normal')
Gr(gr_ts_ba,'b','bad')
Gr(gr_ts_be,'b','belt')
Gr(gr_ts_ro,'b','rota')
Gr(gr_ts_ch,'b','chuk')
'''
plt.plot(gr_xts,'r')
plt.plot(gr_yts,'g')
plt.plot(gr_zts,'b')
plt.show()