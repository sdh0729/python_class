import pandas as pd
from pmdarima.arima import auto_arima

data = pd.read_csv('time/2.2kw_L-EF-04_rotational imbalance.csv', delimiter=',', low_memory=False)

tsx = data['z_axis']
ts = tsx[:500]

model_arima= auto_arima(ts,trace=True, error_action='ignore', start_p=1,start_q=1,max_p=5,max_q=5,suppress_warnings=False,stepwise=False,seasonal=False)
model_arima.fit(ts)