import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('./save/관광수지데이터_201001_201912.json')
plt.rc('font', family='malgun gothic')

df['년도'] = df['날짜'].astype('str').str[:4]
years = df['년도'].unique()

Tourism_ingroup = df.groupby('년도')['관광수입'].sum() // 12
Tourism_outgroup = df.groupby('년도')['관광지출'].sum() // 12
Percapita_ingroup = df.groupby('년도')['인당수입'].sum() // 12
Percapita_outgroup = df.groupby('년도')['인당지출'].sum() // 12

xLabel = '년도'
yLabel = '원'
title1 = '년도별 관광 수입 및 지출'
title2 = '년도별 관광 인당 수입 및 지출'

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(years, Tourism_ingroup, 'b', label='관광수입')
axes[0].plot(years, Tourism_outgroup, 'r--', label='관광지출')
axes[0].set_title(title1)
axes[0].set_ylabel(yLabel)
axes[0].legend()
axes[0].grid(True)

axes[1].plot(years, Percapita_ingroup, 'b', label='인당수입')
axes[1].plot(years, Percapita_outgroup, 'r--', label='인당지출')
axes[1].set_title(title2)
axes[1].set_ylabel(yLabel)
axes[1].legend()
axes[1].grid(True)

plt.xlabel(xLabel)
plt.show()
