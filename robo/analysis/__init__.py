#from analysis import *
# * 의미 : 패키지 내부에 있는 모듈 모두 불러오겠다.
#__all__ : import * 했을 경우에 불러올 패키지 명
from . import series, statics
__all__ = ['series', 'statics']
