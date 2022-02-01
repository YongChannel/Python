from cProfile import label
from matplotlib.lines import _LineStyle
import pandas as pd
import matplotlib.pyplot as plt
import os

ko_df = pd.read_json('./lec21/save/한국_국민해외관광객_201001_202012.json')
jp_df = pd.read_json('./lec21/save/일본_방한외래관광객_201001_202012.json')
cn_df = pd.read_json('./lec21/save/중국_방한외래관광객_201001_202012.json')
am_df = pd.read_json('./lec21/save/미국_방한외래관광객_201001_202012.json')
ko_df.info()
jp_df.info()
cn_df.info()
am_df.info()
#
# # 2010~2020년도 까지 년도별 출/입국자수 그래프 시각화
#
# # 년도별 출/입국자수 구해야함
# # 각 df 년도 칼럼 생성 -> 년도 기준으로 groupby 관광객수의 합계
# ko_df.head()  # 201001 (int)
# # int -> 문자열로 변경하고 앞에 4자리만 가져오기
# ko_df['년도'] = ko_df['날짜'].astype('str').str[:4]
# jp_df['년도'] = jp_df['날짜'].astype('str').str[:4]
# cn_df['년도'] = cn_df['날짜'].astype('str').str[:4]
# am_df['년도'] = am_df['날짜'].astype('str').str[:4]
# # astype():타입을 바꾸는 함수, .str : 문자열 처리 및 함수
#
# ko_df.head()
#
# # 년도별 관광객수 합계
# ko_group = ko_df.groupby('년도')['관광객수'].sum()
# jp_group = jp_df.groupby('년도')['관광객수'].sum()
# cn_group = cn_df.groupby('년도')['관광객수'].sum()
# am_group = am_df.groupby('년도')['관광객수'].sum()
#
# plt.rc('font', family='malgun gothic')
# colorList = ['r', 'b', 'g', 'c']
# xLabel = '년도'
# yLabel = '명'
# title = '년도별 입국/출국자 수'
#
# x = ko_group.index
#
# plt.plot(x, ko_group, 'ro--', label='한국인 출국자 수')
# plt.plot(x, jp_group, 'bv-', label='일본인 출국자 수')
# plt.plot(x, cn_group, 'gs-.', label='중국인 출국자 수')
# plt.plot(x, am_group, 'c*:', label='미국인 출국자 수')
#
# plt.xlabel(xLabel)
# plt.ylabel(yLabel)
# plt.title(title)
# plt.legend()
# plt.grid(True)
# plt.show()
