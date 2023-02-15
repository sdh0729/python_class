import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('time/2.2kw_R-EF-05_belt slack.csv', delimiter=',', low_memory=False)

xts = data['x_axis']
yts = data['y_axis']
zts = data['z_axis']

gr_xts = xts[:500]
gr_yts = yts[:500]
gr_zts = zts[:500]

plt.plot(gr_xts, label='x_axis')
plt.plot(gr_yts, label='y_axis')
plt.plot(gr_zts, label='z_axis')
plt.legend(bbox_to_anchor=(1,1))
plt.title('Belt Slack')
plt.show()