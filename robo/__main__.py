from analysis import *
from crawling.parser import parser_test
import database.connection as dc


#아래 if문은 해당 파일이 main으로 실행됐을때 동작
#다른 파일에서 패키지의 모듈로 불러올 경우 실행을 안함
if __name__ == '__main__':
    #from analysis import *
    #series 와 statics 모듈을 불러옴
    series.series_test() #series의 안에 있는 함수
    statics.statics_test() #statics의 안에 있는 함수

    #from crawling.parser import parser_test
    parser_test() #parser
    
    #import database.connection as dc
    dc.connection_test() #connection
    import database.connection 
    database.connection.connection_test()