# pip install matplotlib
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# 수치계산을 위한 파이썬 라이브러리
# X축, Y축 데이터 만들때 활용

# 그래프 그리기
# 그래프 종류
# (1) 꺽은선 그래프, (2) 수평선/수직선(보조선), (3) 막대 그래프 (4) 수평 막대그래프, (5) 산점도, (6) 히스토그램, (7) 에러바
# (8) 파이차트, (9) 히트맵, (10) 박스플롯, (11) 바이올린 플롯

# 꺽은선 그래프
x = np.arange(0, 4, 0.5)  # arange(시작값,  마지막값, 증감값)
y1 = x + 1
y2 = x ** 2 - 4
y3 = -2 * x + 3
print(x)
print(y1, y2, y3)

print(type(x))
plt.plot(x, y1, color='b', marker='o')
plt.plot(x, y2, color='g', linestyle='--')
plt.plot(x, y3, 'r:')  # X축값, Y축값, 색깔 및 라인 스타일
plt.show()

# 수직선 및 수평선 (보조선)
# 수평선 : axhline(y, xmin, xmax)-비율, hlines(y, xmin, xmax)
# 수직선 : axvline(x, ymin, ymax)-비율, vlines(x, ymin, ymax)

# 수평선
plt.plot(x, y1, color='b', marker='o')
plt.plot(x, y2, color='g', linestyle='--')
plt.plot(x, y3, 'r:')
plt.axhline(2.0, 0.1, 0.9, color='gray', linestyle='--', linewidth=2)  # x축 비율 값 (10%~90%)
plt.hlines(4.0, 0.1, 0.9, color='lightgray', linestyle='solid', linewidth=3)
plt.show()

# 수직선
plt.plot(x, y1, color='b', marker='o')
plt.plot(x, y2, color='g', linestyle='--')
plt.plot(x, y3, 'r:')
plt.axvline(1.0, 0.2, 0.8, color='gray', linestyle='--', linewidth=2)  # y축 비율 값 (20%~80%)
plt.vlines(1.8, -3.0, 2.0, color='lightgray', linestyle='solid', linewidth=3)
plt.show()
# 꺽은선 그래프 x,y축 모두 수치형 데이터인 경우 표시하는 그래프

# 막대그래프
# X축 데이터 범주형데이터(구분을 위한 데이터 ex)혈액형, 년도 등)
# Y축 데이터 수치형 데이터
years = ['2018', '2019', '2020']
values = [100, 400, 900]
plt.bar(years, values)
plt.show()

# 막대 전체 색상 지정
plt.bar(years, values, color='y')
plt.show()

# 막대 개별 색상 지정
plt.bar(years, values, color=['r', 'g', 'y'])
plt.show()

# 막대 폭 지정
plt.bar(years, values, width=0.4)  # 막대 기본폭 0.8
plt.show()

plt.bar(years, values, width=[0.4, 0.8, 1.0])  # 막대 기본폭 0.8
plt.show()

# 막대 기타 스타일 지정
# align : 눈금과 막대 위치 조절(기본값 center), edge 막대의 왼쪽끝 눈금
# edgecolor : 막대 테두리 색
# linewidth : 막대 테두리 두께
plt.bar(years, values, color=['r', 'g', 'y'], width=[0.4, 0.8, 1.0], align='edge', edgecolor='lightgray', linewidth=5)
plt.show()

# 수평막대 그래프
plt.barh(years, values, color=['r', 'g', 'y'], height=[0.4, 0.8, 1.0], align='edge', edgecolor='lightgray', linewidth=5)
plt.show()

# 산점도 그래프
# 두 변수의 상관 관계를 점으로 표현하는 그래프
# 상관관계 두 변수가 얼마나 서로 관련이 있는지
# 양의 상관관계, 음의 상관관계, 무 상관관계

np.random.seed(0)  # 랜덤 시드값 설정(랜덤분포 결정)
n = 50
x = np.random.rand(n)  # 0~1사이의 난수 n개 생성
y = np.random.rand(n)  # 0~1사이의 난수 n개 생성
plt.scatter(x, y)
plt.show()

# 점의 색상와 크기 지정
area = (30 * np.random.rand(n)) ** 2  # 점의 크기(면적)
colors = np.random.rand(n)

# 각 점의 색깔과 크기를 정함
# plt.scatter(x, y, s=area, c=colors)
plt.scatter(x, y, s=15 ** 2, c='y')
plt.show()

# plot과 scatter 차이
plt.plot([1], [1], marker='o', markersize=20, c='r')
plt.scatter([2], [1], s=20 ** 2, c='b')

# text() x,y점 위치에 글자 표시
plt.text(0.5, 1.05, 'plot', fontdict={'size': 15})
plt.text(1.6, 1.05, 'scatter', fontdict={'size': 15})

# axis([x축 최소, x축 최대, y축 최소, y축 최대]) 축의 범위값 설정
plt.axis([0.4, 2.6, 0.8, 1.2])
plt.show()

# 컬러맵
cmaps = plt.colormaps()
# 값에 따른 다양한 컬러 분포를 결정해서 표시

area = (30 * np.random.rand(n)) ** 2  # 점의 크기(면적)
colors = np.random.rand(n)
plt.scatter(x, y, s=area, c=colors, cmap='Spectral', alpha=0.5)

# alpha : 투명도
plt.colorbar()
plt.show()

# 히스토그램
# 도수분포표를 그래프로 나타낸것, 가로축은 계급, 세로축은 도수(횟수,갯수)
# 도수분포표는 1차원 데이터의 계급(구간)별 갯수를 시각화함
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71, 80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
plt.hist(weight)
plt.show()

# bins : 구간 개수 지정
min(weight), max(weight)

# bins = 10
# 계급 크기 : 2.5 = (81-56)/10
# 첫 계급구간 : 56~ 56+(81-56)/10 => 56 ~ 58.5
plt.hist(weight, bins=10, label='bins=10')
plt.legend()  # 범례표시(그래프 라벨)
# x축 눈금값 설정

bins = 10
xtickList = [min(weight) + (max(weight) - min(weight)) / bins * i for i in range(bins + 1)]
plt.xticks(xtickList, xtickList)

# xticks(눈금위치 리스트, 눈금에 표시할값 리스트)
plt.show()

# 누적 히스토그램
plt.hist(weight, bins=10, cumulative=True, label='cu_True')
plt.hist(weight, bins=10, cumulative=False, label='cu_False')
plt.xticks(xtickList, xtickList)
plt.legend()
plt.show()

# 정규화 => 도수(비율), 전체의 몇퍼센트
# plt.hist(weight, bins=10, cumulative=True, label='cu_True', density=True)
plt.hist(weight, bins=10, cumulative=False, label='cu_False', density=True)
plt.xticks(xtickList, xtickList)
plt.legend()
plt.show()

# 에러바 표시
# 데이터의 편차를 표시하기 위한 그래프
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
yerr = [2.3, 3.1, 1.7, 2.5]  # 데이터 포인트 위/아래 대칭인 오차를 표시
plt.errorbar(x, y, yerr=yerr)
plt.show()
# 편차 : 데이터와 데이터중심지표(평균, 중앙값, 최빈값)와 차이

# 비대칭 편차
yerr = [[2.3, 3.1, 1.7, 2.5], [1.1, 2.5, 0, 3.9]]  # 아래방향편차, 윗방향편차
plt.errorbar(x, y, yerr=yerr)
plt.show()

# 상한/하한 기호 표시
yerr = np.linspace(0.4, 0.8, 4)  # 0.4 ~ 0.8까지 균등한 간격으로 4개의 점
yerr  # array([0.4 , 0.53333333, 0.66666667, 0.8])
upperLimits = [True, False, True, False]
lowerLimits = [True, False, False, True]
x = np.arange(1, 5)
y = x ** 2
plt.errorbar(x, y, yerr=yerr, uplims=upperLimits, lolims=lowerLimits)
plt.show()

# 파이차트
# 범주별 구성 비율을 원형으로 표현한 그래프
values = [77, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False)
plt.show()

# 각 파이별 중심에서 벗어나는 정도 설정
explode = [0, 0.1, 0, 0.1]  # 반지름의 비율
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False, explode=explode)
plt.show()

# 그림자 및 파이의 색깔지정
colors = ['silver', 'gold', 'whitesmoke', 'lightGray']
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False, explode=explode, showdow=True,
        colors=colors)
plt.show()

# 부채꼴 스타일 지정
wedgeprops = {'width': 0.7, 'edgecolor': 'r', 'linewidth': 5}  # width반지름비율
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False, explode=explode, shadow=True,
        colors=colors, wedgeprops=wedgeprops)
plt.show()

# 히트맵
# 다양한 값을 갖는 숫자 데이터를 열분포 형태와 같이 색상을 이용해 시각화
arr = np.random.standard_normal((30, 40))  # 표준 정규분포의 분포값 랜덤 추출

# 2차원 데이터
arr.shape  # (30, 40) => 30행 40열의 데이터
plt.matshow(arr)
plt.show()

# 컬러바 표시
plt.matshow(arr)
plt.colorbar()
plt.show()

# 색상범위 지정
plt.matshow(arr)
plt.colorbar(shrink=0.8, aspect=10)
# shrink : 컬러바 크기, 디폴트1
# aspect : 컬러바 종횡비, 디폴트 20

plt.clim(-1.0, 1.0)  # 컬러바 범위 설정
plt.show()

# 컬러맵 지정
plt.colormaps()  # 컬러맵 확인
plt.matshow(arr, cmap='Reds')
plt.colorbar(shrink=0.8, aspect=10)
plt.clim(-1.0, 1.0)  # 컬러바 범위 설정
plt.show()

# 박스플롯
# 박스플롯은 1차원 데이터의 분포를 한눈에 확인 가능
# 중앙값, 사분위범위, 이상치 등 확인 가능

# 평균 0, 표준편차2인 정규분포에서 1000개샘플
data_a = np.random.normal(0, 2.0, 1000)
# 평균 -3.0, 표준편차1.5인 정규분포에서 500개샘플
data_b = np.random.normal(-3.0, 1.5, 500)
# 평균 1.2, 표준편차1.5인 정규분포에서 1500개샘플
data_c = np.random.normal(1.2, 1.5, 1500)

plt.boxplot([data_a, data_b, data_c])
plt.xlabel('Data Type')  # x축 라벨 지정
plt.ylabel('Value')  # y축 라벨 지정
plt.ylim(-10, 10)  # y축 하한, 상한 범위 지정
plt.show()

# 박스플롯에서 사분위 수, 중앙값 등을 얻기
box = plt.boxplot([data_a, data_b, data_c])

# (Q1, min), (Q3, max)
whiskers = [item.get_ydata() for item in box['whiskers']]
# 총 데이터가 3개여서 각각 값을 얻기

# 총 6개의 데이터
whiskers[0]  # 0번째 데이터의 (Q1,min)
whiskers[1]  # 0번째 데이터의 (Q3,max)
whiskers[2]  # 1번째 데이터의 (Q1,min)
whiskers[3]  # 1번째 데이터의 (Q3,max)
whiskers[4]  # 2번째 데이터의 (Q1,min)
whiskers[5]  # 2번째 데이터의 (Q3,max)

# 중앙값
medians = [item.get_ydata() for item in box['medians']]
# 각 데이터별 (평균값, 중앙값)

# 이상치
fliers = [item.get_ydata() for item in box['fliers']]
len(fliers)
fliers[0]  # 0번째 데이터의 이상치값들
fliers[1]  # 1번째 데이터의 이상치값들
fliers[2]  # 2번째 데이터의 이상치값들

# 수평 박스 플롯 그리기
plt.boxplot([data_a, data_b, data_c], vert=False)
plt.xlabel('Value')  # x축 라벨 지정
plt.ylabel('Data Type')  # y축 라벨 지정
plt.xlim(-10, 10)  # x축 하한, 상한 범위 지정
plt.show()

# 바이올린 플롯
# 박스플롯 + 히스토그램
plt.violinplot([data_a, data_b, data_c], positions=[2, 3, 4])
# positions : 바이올린 플롯의 x축 위치

plt.xlabel('Data Type')  # x축 라벨 지정
plt.ylabel('Value')  # y축 라벨 지정
plt.ylim(-10, 10)  # y축 하한, 상한 범위 지정
plt.show()

# 평균값, 중앙값, 최대/최소 표현
plt.violinplot([data_a, data_b, data_c], positions=[2, 3, 4], showmeans=True, showmedians=True, showextrema=True)
plt.xlabel('Data Type')  # x축 라벨 지정
plt.ylabel('Value')  # y축 라벨 지정
plt.ylim(-10, 10)  # y축 하한, 상한 범위 지정
plt.show()

# 분위수 지정하기
plt.violinplot([data_a, data_b, data_c], positions=[2, 3, 4], showmeans=True, showmedians=True, showextrema=True,
               quantiles=[(0.25, 0.5, 0.75), (0.1, 0.9), (0.3, 0.5, 0.7)])
plt.xlabel('Data Type')  # x축 라벨 지정
plt.ylabel('Value')  # y축 라벨 지정
plt.ylim(-10, 10)  # y축 하한, 상한 범위 지정
plt.xticks([2, 3, 4], ['A', 'B', 'C'])
plt.show()

# 스타일 지정
violin = plt.violinplot([data_a, data_b, data_c], positions=[2, 3, 4], showmeans=True, showmedians=True,
                        showextrema=True, quantiles=[(0.25, 0.5, 0.75), (0.1, 0.9), (0.3, 0.5, 0.7)])
# bodies : 각 바이올린 분포의 채워진 영역
# cmeans : 평균값
# cmins : 최솟값
# cmaxes : 최댓값
# cbars : 중심 수직선
# cmedians : 중앙값
# cquantiles :분위값

violin['bodies'][0].set_facecolor('blue')
violin['bodies'][1].set_facecolor('red')
violin['bodies'][2].set_facecolor('green')
violin['cmaxes'].set_edgecolor('gray')
violin['cmins'].set_edgecolor('gray')
violin['cquantiles'].set_edgecolor('pink')
plt.xlabel('Data Type')  # x축 라벨 지정
plt.ylabel('Value')  # y축 라벨 지정
plt.ylim(-10, 10)  # y축 하한, 상한 범위 지정
plt.xticks([2, 3, 4], ['A', 'B', 'C'])
plt.show()

# 한창에 여러 개의 그래프를 각각 그리는 방법
fig, axes = plt.subplot(2, 2)  # 행 2개 열 2개 총 4개 그래프 출력
plt.show()

# 창 크기 및 축 공유
fig, axes = plt.subplot(2, 2, figsize=(5, 5), sharex=True, sharey=True)  # 행 2개 열 2개 총 4개 그래프 출력
plt.show()

# 그래프 그리기
x = np.arange(1, 5)
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, squeeze=True)
axes[0][0].plot(x, np.sqrt(x), c='gray', linewidth=3)
axes[0][1].plot(x, x, c='g^-', markersize=3)
axes[1][0].plot(x, -x + 5, 'ro--', linewidth=1)
axes[1][1].plot(x, np.sqrt(-x + 5), 'b.-.')
plt.show()

# 각 그래프에 제목 및 범례표시
x = np.arange(1, 5)
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, squeeze=True)
axes[0][0].plot(x, np.sqrt(x), c='gray', linewidth=3, label='y=sqrt(x)')
axes[0][0].set_title('Graph1')  # 제목 표시
axes[0][0].legend()  # 범례표시
axes[0][0].grid(True)  # 격자무늬 배경으로 표시

axes[0][1].plot(x, x, 'g^-', markersize=3, label='y=x')  # 색상-마커-선스타일
axes[0][1].set_title('Graph2')  # 제목 표시
axes[0][1].legend()  # 범례표시
axes[0][1].grid(True)  # 격자무늬 배경으로 표시

axes[1][0].plot(x, -x + 5, 'ro--', linewidth=1, label='y=-x+5')
axes[1][0].set_title('Graph3')  # 제목 표시
axes[1][0].legend()  # 범례표시

axes[1][1].plot(x, np.sqrt(-x + 5), 'b.-.', label='y=sqrt(-x+5)')
axes[1][1].set_title('Graph4')  # 제목 표시
axes[1][1].legend()  # 범례표시
plt.show()

# 하나의 ax 그래프 창에 두개의 그래프를 y축을 다르게해서 표시
# y축이 왼쪽, 오른쪽 2개로 생성
x = np.arange(0, 3)
y1 = x + 2
y2 = -x - 1
fig, ax = plt.subplots()
ax.plot(x, y1, c='g')

ax.plot(x, y2, c='deepping')
plt.show()

# 하나의 ax 그래프 창에 두개의 그래프 표시
# x축, y축 공유가 되서 그래프 표시
x = np.arange(0, 3)
y1 = x + 2
y2 = -x - 1
fig, ax = plt.subplots()
ax.plot(x, y1, c='g', label='y=x+2')
ax.plot(x, y2, c='deeppink', label='y=-x-1')
plt.legend()
plt.show()

# 2중 y축 생성 : y축이 왼쪽, 오른쪽 2개로 생성됨
x = np.arange(0, 3)
y1 = x + 2
y2 = -x - 1
fig, ax = plt.subplots()
ax.plot(x, y1, c='g', label='y=x+2')
ax2 = ax.twinx()
ax2.plot(x, y2, c='deeppink', label='y=-x-1')
ax.legend(loc='upper right')  # 오른쪽 위
ax2.legend(loc='lower left')  # 왼쪽 아래
plt.show()

# 범례를 합쳐서 표시
x = np.arange(0, 3)
y1 = x + 2
y2 = -x - 1
fig, ax = plt.subplots()
line = ax.plot(x, y1, c='g', label='y=x+2')
ax2 = ax.twinx()
line2 = ax2.plot(x, y2, c='deeppink', label='y=-x-1')
lines = line + line2
labels = [l.get_label() for l in lines]
labels  # ['y=x+2', 'y=-x-1']
ax.legend(lines, labels, loc='upper right')  # 오른쪽 위
plt.show()

# 꺽은그래프와 막대그래프를 한창에 출력
x = np.arange(2020, 2027)
y1 = np.array([1, 3, 7, 5, 9, 7, 14])
y2 = np.array([1, 3, 5, 7, 9, 11, 13])

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y1, 'g-s', markersize=7, linewidth=5, alpha=0.7, label='price')
ax.set_ylim(0, 18)
ax.set_xlabel('Year')
ax.set_ylabel('Price($)')
ax.tick_params(axis='both', direction='in')  # 축 틱 방향 설정

ax2 = ax.twinx()  # x축 공유, y축 다르게
ax2.bar(x, y2, color='deeppink', label='Demand', alpha=0.7, width=0.7)
ax2.set_ylim(0, 18)
ax2.set_ylabel(r'Demand ($\times10^6$)')  # 수학적 표현 되도록 하는 기능
ax2.tick_params(axis='y', direction='in')

ax.legend(loc='upper left')
ax2.legend(loc='upper right')

ax.set_zorder(ax2.get_zorder() + 10)  # ax가 ax2보다 위에 표시되도록함
ax.patch.set_visible(False)  # 뒤에 막대그래프도 출력되도록 함
plt.show()

# 수학적 표현 $수학기호식$
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.text(1, 15, r'$\alpha^3 > \beta_5 \pi \sin(x)$')
plt.show()

# 한글 표시 : 폰트 설정을 안하면 깨짐
plt.rc('font', family='malgun gothic')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.text(1, 15, r'$\alpha^3 > \beta_5 \pi \sin(x)$')
plt.title("한글 제목입니다.")
plt.show()

# 이미지 저장
plt.figure(linewidth=2)  # 창 두께
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
plt.plt(x1, y1, 'o-')

import os

path = './lec21/save'
if not os.path.exists(path): os.makedirs(path)

plt.savefig(path + '/그래프1.png', dpi=200)  # dpi는 해상도(기본값 100)

# 배경색 및 테두리색
plt.savefig(path + '/그래프1.png', dpi=200, facecolor='#eeeeee', edgecolor='')

# 여백 최소화
plt.savefig(path + '/그래프_여백최소화.png', bbox_inches='tight')

# 여백 최소화후 패딩(안에 여백)
plt.savefig(path + '/그래프_여백최소화.png', bbox_inches='tight', pad_inches=0.5)
