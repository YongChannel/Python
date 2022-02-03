import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./save/주요발생국가주간동향(4월2째주).csv', index_col='국가')
df.head()

X = df.index  # 국가명
Y = df['4월06일']
# 각 막대의 컬러
colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'silver', 'violet', 'indigo']
xLabel = '국가명'
yLabel = '발생건수'
title = '4/6일 국가별 코로나 발생건수'

# 폰트설정
plt.rc('font', family='malgun gothic')

# 각 국가별 코로나 발생건수 비율 데이터
ratioList = Y / Y.sum() * 100
ratioList

# bar그래프 그리기
plt.bar(X, Y, color=colorList, alpha=0.7)  # alpha는 투명도값

# 비율과 발생건수 텍스트를 bar그래프에 출력
for i in range(len(Y)):
    # 발생건수 텍스트
    # f'{숫자:,} : 1,000 숫자 천자리마다 콤마로 표시가 됨
    plt.text(x=i, y=Y[i] + 1000, s=f'{Y[i]:,}건', horizontalalignment='center', fontdict={'size': 7})
    # horizontalalignment : 글자 수평방향 정렬
    # fontdict : 글자 폰트, 사이즈 등 변경

    # 비율 텍스트
    plt.text(x=i, y=Y[i] / 2 - 1000, s=f'{ratioList[i]:.1f}%', horizontalalignment='center', fontdict={'size': 7})

# 수평선
mean = Y.mean()
plt.axhline(y=mean, color='r', linewidth=1, linestyle='--')
# 평균값 텍스트
plt.text(x=X.size - 1, y=mean + 2000, s=f'평균 : {mean:,}건', horizontalalignment='center', fontdict={'size': 8})

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.xticks(fontsize=8)
plt.savefig('./save/4월6일 국가별 코로나 발생건수.png', dpi=200)
plt.show()
