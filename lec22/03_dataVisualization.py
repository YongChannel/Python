# import imp
import pandas as pd
import folium

df = pd.read_csv('./save/홀리스카페_위도경도.csv')
df.head()
df.info()

# 지도생성
m = folium.Map(location=[df.loc[0, '위도'], df.loc[0, '경도']], zoom_start=7)

# 마커 생성
from folium.plugins import MarkerCluster

m_cluster = MarkerCluster().add_to(m)  # 마커 클러스터 객체 생성

for i, data in df.iterrows():  # 데이터 프레임 반복문
    if data['위도'] == 0:
        continue
    else:
        folium.Marker(
            location=[data['위도'], data['경도']],
            popup=data['매장명'],
            icon=folium.Icon(icon='star', color='blue')
        ).add_to(m_cluster)
m.save('./save/홀리스카페_map.html')
