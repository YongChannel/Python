import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./save/주요발생국가주간동향(4월2째주).csv', index_col='국가')
df.head()

x = df.index
y = df['4월06일']

plt.rc('font', family='malgun gothic')

fig, axes = plt.subplots(1, 1, sharex=True, sharey=True, squeeze=True)
axes.set_title('4/6일 국가별 코로나 발생건수')

key = [i for i in x]
value = [j for j in y]

print(key)
print(value)

plt.bar(key, value, color=['b', 'g', 'r', 'c', 'm',
                           'y', 'k', 'silver', 'violet', 'indigo'])
y = sum(value) / len(key)

plt.axhline(y, color='red', linestyle='--', linewidth=2)

plt.show()
