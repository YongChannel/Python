from turtle import fillcolor
import folium
from folium.map import Icon

# 초기 위치가 세팅된 지도 만들기
m = folium.Map(
    location=[37.25059686245495, 127.02286427731822],  # 위도,경도
    zoom_start=15  # 지도 초기 위치 확대값(기본값 10)
)

# 지도상에 마커표시(아이콘)
# folium.Marker(
#     location=[37.25059686245495, 127.02286427731822],
#     popup='엠아이티능력개발원',
#     icon=folium.Icon(icon='star', color='red')
# ).add_to(m)

# 지도상에 원형마커 표시
folium.CircleMarker(
    location=[37.25059686245495, 127.02286427731822],
    popup='엠아이티능력개발원',
    icon=folium.Icon(icon='star', color='red'),
    radius=100,  # 반경
    color='#ffffgg',  # 테두리 색깔
    fill_color='#ffffgg'  # 원 내부 색깔
).add_to(m)

# 마커클러스터 : 지도 확대/축소에 따라 마커들을 묶어주고/펼침
latlon = [[37.31355679999999, 127.08034150000003], [37.35959300000016, 127.105316],
          [37.388204699999996, 126.66208460000007], [37.19821445962207, 127.07333060688757],
          [37.3862876275833, 126.96253325015414], [37.31864776315991, 127.08885641049494],
          [37.56661020000001, 126.97838810000007]]
from folium.plugins import MarkerCluster

m_cluster = MarkerCluster().add_to(m)  # 마커클러스터 객체 생성, 지도에 추가
for i, pos in enumerate(latlon):
    folium.Marker(
        location=pos,
        popup=str(i),
        icon=folium.Icon(icon='info-sign', color='darkblue')
    ).add_to(m_cluster)  # 각 마커들은 마커클러스터 추가

# 시도의 경계를 표시
# geojson 파일 활용 경계표시 - 인터넷 사용
import json

with open('./save/seoul_muncipalities_geo.json', 'r', encoding='utf-8') as f:
    seoulGeo = json.loads(f.read())
folium.GeoJson(
    seoulGeo,
    name='서울특별시'
).add_to(m)

# 도별 경계를 표시
with open('./save/TL_SCCO_CTPRVN.json', 'r', encoding='utf-8') as f:
    geo = json.loads(f.read())
folium.GeoJson(
    geo
).add_to(m)

# 지도 저장
import os
path = './save'
if not os.path.exists(path) :
    os.makedirs(path)
m.save(os.path.join(path, '엠아이티능력개발원.html'))
