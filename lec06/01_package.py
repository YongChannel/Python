# 서로 다른 패키지의 경로에 있는 모둘을 불러오기 위해서 경로 추가를 해야함
import sys

sys.path.append('C:/works/python')
from robo import *

# try:
#     from robo import *
# 최상위 프로젝트 폴더가 기본 경로
# except:
#     from ..robo import *
# 이 파일은 기본문법 패키지, robo는 다른 패키지에 있다
analysis.series.series_test()
crawling.parser.parser_test()
database.connection.connection_test()
