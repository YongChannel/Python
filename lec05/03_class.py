# 1. 내장함수
# 숫자
sum()  # 반복 가능한 자료형list, set등의 합계 계산
abs()  # 절댓값을 돌려주는 함수
divmod(a, b)  # a를 b로 나눈 몫과 나머지를 튜플로 반환
hex()  # 정수를 입력받아 16진수로 변환
oct()  # 정수를 입력받아 8진수로 변환
int(x, radix)  # radix 진수 문자열을 10 진수로 반환
round(숫자, 자릿수)  # 숫자를 입력받아 반올림 해주는 함수
max()  # 자료형의 최댓값
min()  # 자료형의 최솟값

# 논리
# all() # 반복 가능한 자료형 모든 요소들이 참이면 True 하나라도 거짓이면 False()
all([True, False])
all([True, True])
all([1, 2, 3, -1])  # 숫자가 모두 0이 아니면 True
all([1, 2, 3, 0])  # 숫자가 하나라도 0이면 False

# any() # 반복 가능한 자료형 모든 요소들이 하나라도 참이면 True 모두 거짓이면 False
any([True, False])
any([False, False])
any([1, 2, 0])
any([0, 0, 0])

# 0, '', False는 모두 False로 처리됨 나머지는 True

# 윤년 확인
year = 2020
print(all([year % 4 == 0, any([year % 100 != 0, year % 400 == 0])]))

# 타입 체크
# isinstance(데이터, 타입)
print(isinstance('aa', str))
print(type('hello') == str)

# eval(문자열)
# 실행 가능한 문자열을 입력으로 실행한 결과를 반환
# 문자열로 함수나 클래스 등 동적으로 실행 가능
print(eval('1 + 2 + 3 * 5'))
print(eval("'hello' + 'world'"))
print(eval("[i for i in range(10)]"))
print(eval("sum([1, 2, 3, 4, 5])"))

# 2. 외장 라이브러리
# sys 모듈
# 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import sys

# sys.argv: 명령행 인수로 프로그램 실행시 인수 전달 가능
print(sys.argv)

# sys.exit()
# 강제로 스크립트 종료
for i in range(10):
    print(i)
    if i == 5:
        sys.exit()

# sys.path
# 자신이 만든 도뮬을 불러와 사용
print(sys.path)

from pprint import pprint

pprint(sys.path)

# 특정 경로에 라이브러리를 만든경우
# 경로를 추가해야함
# sys.path.append(라이브러리경로)
sys.path.append('C:/Desktop')

# os 모듈
# 환경변수나 디렉토리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
import os

os.getcwd()  # 현재 경로 얻기
os.chdir('C:')  # 디렉토리 위치 변경
os.getcwd()
os.system('ipconfig')  # 도스명령어로 네트워크 정보 확인
os.mkdir(경로)  # 해당 경로에 폴더 만들기
os.makedirs(경로)  # 해당 경로에 모든 폴더 만들기
os.rmdir(경로)  # 디렉토리 삭제
os.unlink(경로)  # 파일 삭제
os.rename(src, dst)  # src 이름의 파일을 dst로 변경

# random 난수를 발생시키는 모듈
import random

random.random()

fruits = ['사과', '딸기']
random.shuffle(fruits)  # 리스트를 섞음
random.choice(fruits)  # 리스트 항목 중 무작위로 하나 뽑음

# 시간 관련
import time

time.time()
# 1970년 1월 1일 0시 0분 0초 기준
# 지난 시간을 초 단위로 반환

time.localtime(time.time())
# time.time()이 돌려준 실수 값을 년 월 일 시 분 초로 반환
time.localtime(time.time()).tm_year
time.localtime(time.time()).tm_mon

time.asctime(time.localtime(time.time()))
# localtime에서 반환된 값을 알아보기 쉬운 문자열 형태의 날짜/시간으로 반환
time.ctime()  # 현재시간 문자열로 반환

time.sleep(1)  # 정해진 시간만큼 대기
for i in range(5):
    print(i)
    time.sleep(1)

# datetime 모듈 날짜시간 관련
from datetime import datetime, timedelta

time1 = datetime(2022, 1, 18, 16, 27, 0)
time2 = datetime.now()
print(time1, time2)
