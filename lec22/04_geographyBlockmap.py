import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 그래프 폰트 변경
plt.rc('font', family='malgun gothic')
# 블록맵 행정구역 경계선 x,y 데이터
BORDER_LINES = [
    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)],  # 인천
    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
     (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)],  # 경기도
    [(9, 12), (9, 10), (8, 10)],  # 강원도
    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
     (13, 4), (14, 4), (14, 2)],  # 충청남도
    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
     (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)],  # 충청북도
    [(14, 4), (15, 4), (15, 6)],  # 대전시
    [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)],  # 경상북도
    [(14, 8), (16, 8), (16, 10), (15, 10),
     (15, 11), (14, 11), (14, 12), (13, 12)],  # 대구시
    [(15, 11), (16, 11), (16, 13)],  # 울산시
    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)],  # 전라북도
    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)],  # 광주시
    [(18, 5), (20, 5), (20, 6)],  # 전라남도
    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)],  # 부산시
]


# 블록맵의 블록에 데이터 매핑 후 색을 표시하여 블록맵 그리는 함수
def draw_blockMap(blockedMap, targetData, filePath, color):
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])
    datalabel = targetData

    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(8, 13))
    temptitle = filePath.split('\\')[-1].split('.')[0]
    plt.title(temptitle)
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=color, edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'

        if row.isna()[0]:
            continue

        dispname = row['shortName']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 7.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=4)

    plt.gca().invert_yaxis()
    # plt.gca().set_aspect(1)
    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()

    plt.savefig(filePath)
    plt.show()


# 데이터 불러오기
path = './save'
hollys = pd.read_csv(path + '/홀리스카페_위도경도.csv')
hollys.info()

# 홀리스카페 주소 -> 시도와 군구 데이터 생성
hollys['전처리_주소'][0]
# '서울특별시 강남구 테헤란로 301 역삼동 701-02 삼정빌딩 1층'
# 방법 : split() 공백을 자른후 리스트로 반환, 리스트의 0번째 시도, 1번째 군군
'서울특별시 강남구 테헤란로 301 역삼동 701-02 삼정빌딩 1층'.split()[:2]

addrList = hollys['전처리_주소'].apply(lambda x: x.split()[:2]).to_list()
addrs = pd.DataFrame(addrList, columns=['시도', '군구'])
addrs.head()

# 데이터 전처리
addrs['시도'].unique()
addrs['시도'].replace('서울', '서울특별시', inplace=True)
# inplace=True, 원본데이터 변경
addrs['시도'].replace('서울시', '서울특별시', inplace=True)
addrs['시도'].replace('대전', '대전광역시', inplace=True)
addrs['시도'].replace('충북', '충청북도', inplace=True)
addrs['시도'].replace('경북', '경상북도', inplace=True)
addrs['시도'].replace('경남', '경상남도', inplace=True)
addrs['시도'].replace('경기', '경기도', inplace=True)
addrs['시도'].replace('울산', '울산광역시', inplace=True)
addrs['시도'].replace('전북', '전라북도', inplace=True)
addrs['시도'].replace('강원', '강원도', inplace=True)
addrs['시도'].replace('대구시', '대구광역시', inplace=True)
addrs['시도'].replace('대구', '대구광역시', inplace=True)
addrs['시도'].replace('전남', '전라남도', inplace=True)
addrs['시도'].replace('인천', '인천광역시', inplace=True)
addrs['시도'].replace('세종', '세종특별자치시', inplace=True)
addrs['시도'].replace('부산', '부산광역시', inplace=True)
addrs['시도'].unique()

addrs['군구'].unique()  # 금송로, 나성로, 절재로
addrs[addrs['군구'] == '금송로']  # 36  세종특별자치시  금송로
addrs[addrs['군구'] == '나성로']  # 161  세종특별자치시  나성로
addrs[addrs['군구'] == '절재로']  # 386  세종특별자치시  절재로

# loc[인덱스명, 칼럼명]
addrs.loc[36, '군구'] = '세종시'
addrs.loc[161, '군구'] = '세종시'
addrs.loc[386, '군구'] = '세종시'
addrs['군구'].unique()

# 시도군구별 매장개수
# 시도군구 칼럼 생성
addrs['시도군구'] = addrs['시도'] + " " + addrs['군구']

# Groupby를 통한 시도군구별 매장개수
addrs['개수'] = 0
addr_group = addrs.groupby(['시도군구', '시도', '군구'], as_index=False)['개수'].count()

# 시도군구 칼럼을 인덱스 설정
addr_group.set_index('시도군구', inplace=True)

# 홀리스카페 정보 + 인구 데이터 병합
pop = pd.read_excel('./save/행정구역_시군구_별__성별_인구수_20220126091739.xlsx')
# dependency 'openpyxl'.  Use pip or conda to install openpyxl.
# pip install openpyxl
pop.info()
pop.head()

# 데이터 전처리
pop['시도'] = pop['시도'].str.strip()
pop['군구'] = pop['군구'].str.strip()
# pop['군구'] = pop['군구'].strip() #오류

# 시도군구 칼럼 생성 및 인덱스화
pop['시도군구'] = pop['시도'] + " " + pop['군구']
# 소계 데이터 제거
pop = pop[pop['군구'] != '소계']
pop.set_index('시도군구', inplace=True)
pop.head()

# 데이터 병합
# merge() : 열방향으로 같은 인덱스끼리 데이터 결합
# 병합방법 : 내부조인(서로 인덱스가 같은 데이터 기준으로 병합), 외부조인(서로 인덱스가 다른 데이터가 있어도 같이 병합)

addr_pop = pd.merge(addr_group, pop, how='inner', left_index=True, right_index=True)
addr_pop.head()
addr_pop = addr_pop[['시도_x', '군구_x', '총인구수', '개수']]
addr_pop.head()

# 칼럼이름 수정
addr_pop.columns = ['시도', '군구', '총인구수', '개수']
addr_pop.head()

# 인구 십만명당 매장 개수
addr_pop['인구당개수'] = addr_pop['개수'] / addr_pop['총인구수'] * 10 ** 5
addr_pop.head()

# 블록맵 지리정보와 기존데이터와 병합
data_korea = pd.read_csv('./save/data_draw_korea.csv', index_col=0)
data_korea.head()

# 시도군구 칼럼 생성
data_korea['시도군구'] = data_korea['광역시도'] + " " + data_korea['행정구역']
data_korea.set_index('시도군구', inplace=True)
data_korea.head()

# 기존데이터와 병합(외부조인)
data_all = pd.merge(data_korea, addr_pop, how='outer', left_index=True, right_index=True)
data_all.head()

# 블록맵 위치 좌표가 없는 데이터 확인
data_all[data_all['x'].isnull()]
data_all = data_all[data_all['x'].notnull()]

# 행정구역별 매장개수 블록맵 시각화
# draw_blockMap(data, 표시할 속성명, 저장경로, 색깔맵)
draw_blockMap(data_all, '개수', './save/행정구역별 홀리스카페 블록맵.png', 'Blues')

# 행정구역별 인구수 10만명당 매장수 시각화
draw_blockMap(data_all, '인구당개수', './save/행정구역별 인구수 10만명당 홀리스카페 블록맵.png', 'Reds')
data_all['면적']  # *10^6(m2) 생략

# 행정구역별 면적 10^7(m2)당 매장 개수 시각화
# 면적별개수 칼럼생성
# Greens 컬러맵 표시

data_all['면적당개수'] = data_all['개수'] / data_all['면적'] * 10
data_all['면적당개수'].head()
draw_blockMap(data_all, '면적당개수', './save/행정구역별 면적당 갯수 홀리스카페 블록맵.png', 'Greens')
