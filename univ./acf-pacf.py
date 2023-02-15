import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

data = pd.read_csv('time/2.2kw_L-EF-04_rotational imbalance.csv', delimiter=',', low_memory=False)

xts = data['x_axis']
yts = data['y_axis']
zts = data['z_axis']
gr_xts = xts[:500]
gr_yts = yts[:500]
gr_zts = zts[:500]

plot_acf(gr_xts)
plot_pacf(gr_xts)
plot_acf(gr_yts)
plot_pacf(gr_yts)
plot_acf(gr_zts)
plot_pacf(gr_zts)
plt.show()
