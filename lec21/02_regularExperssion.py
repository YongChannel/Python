# 1. 정규 표현식
# 문자열의 패턴 매칭, 문자열 검색, 파싱, 문자열 바꿈 등에서 활용
# 모든 프로그래밍 언어에서 활용

# . : 글자 하나를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝
# ? : 앞문자가 있어도 되고 없어도 됨 ex) appl?e => appe, apple
# (?i) : 대소문자 구분안함
# | : 다자 택일 (OR 조건) ex) a|bpple => apple, bpple

# 반복기호
# + : 1번 이상을 의미 ex) a+pple =>apple, aapple, aaapple 등
# * : 0번 이상을 의미 ex) a*pple => pple, apple, aaaaaaapple 등
# {m,n} : m번 이상 n번이하 반복 ex) ca{2,4}t => caat, caaat, caaaat
# {m} : m번 반복 ex) a{4} => aaaa

# 문자클래스
# [] : []사이의 문자 하나와 매치 ex) [abc]pple => apple, bpple, cpple

# 문자클래스 특수 용도
# [0-9] : [012345789] => 숫자 하나와 매치
# [a-z] : 알파벳 소문자 하나와 매치
# [A-Z] : 알파벳 대문자 하나와 매치
# [a-zA-Z] : 모든 알파벳 하나와 매치
# [ㄱ-ㅎㅏ-ㅣ가-힣] : 모든 한글 하나와 매치
# [가-힣] : 한글 글자 하나와 매치
# [^문자집합] : 해당 문자들과 아닌것과 매치 ex) [^abc]pple => dpple, fpple 등

# \d : 숫자와 매치 [0-9]와 같음
# \D : 숫자가 아닌것과 매치 [^0-9]와 같은
# \w : 문자,숫자,"_"와 매치
# \W : 문자,숫자,"_"가 아닌것과 매치
# \s : whiteSpace 문자와 매치 [ \t\b\r\f\v]
# \S : whiteSpace 아닌것과 매치

# 정규표현식 앞에 r'' 사용
# \b : 단어의 경계(공백, 탭, 컴마, 대시등)과 매치
# \B : 단어의 경계가 아닌것과 매치

# 그룹 () : () 사이의 모든 문자와 매칭 및 그룹 기능

# 2. 파이썬 re모듈 함수
# match() : 문자열의 처음부터 끝까지 정규식와 매치되는지 조사
# search() : 문자열의 전체를 검색하여 정규식과 매치되는 문자열 조사
# findall() : 정규식과 매치되는 모든 문자열 리스트로 반환
# split() : 정규식과 매치되는 문자열 기준으로 파싱하여 리스트로 반환
# sub() : 정규식과 매치되는 문자열을 다른 문자열로 바꿈

import re

## match()
# text = 'abc연아'
# m = re.match(r'..연아', text)
# if m != None:
#     print(m.group())  # 매치된 문자열 반환
# else:
#     print(m)  # 매치된 결과가 없으면 None
#
# textList = ['김연아', 'aaa연아', 'cc연아']
# for txt in textList:
#     m = re.match(r'...연아', txt)
#     if m != None:
#         print(f'{txt} 매치')
#     else:
#         print(f'{txt} 매치 안됨')

## 주민번호 매치
# text = '881009-1234567'
# m = re.match(r'\d{6}-\d{7}', text)
# if m != None:
#     print(m.group())
# else:
#     print(text)

## 휴대폰 번호와 매치
# textList = ['010-3141-1233', '016-3141-1233', '010-4444-123', '010-444-1234', '010-4444-12345']
#
# for txt in textList:
#     m = re.match(r'^[0-1]{3}-\d{4}-\d{4}$', txt)
#     if m != None:
#         print(m.group())
#     else:
#         print(m)


## search()
## 특정한 패턴을 가진 문자열 검색
# text = 'Good care, Care'
# m = re.search(r'...d', text)
# print('일치하는 문자열 :', m.group())
# print('일치하는 문자열의 시작 인덱스 :', m.start())
# print('일치하는 문자열의 끝 인덱스 :', m.end())
# print('일치하는 문자열의 시작과 끝 인덱스 튜플 :', m.span())


## findall()
## 특정한 패턴과 일치하는 모든 문자열 리스트로 반환
# text = 'berry 1berry 10berry apple strawberry'
# mList = re.findall(r'\w*berry', text)
# print(mList)

## a태그의 href값 찾기
# text = "<a href='www.naver.com'></a> <a href='www.daum.net'></a>"
# mList = re.findall(r"\'[\w\.]+\'", text)
# print(mList)

## line과 일치하지만 line을 포함하는 글자들은 매치되지 않도록 검색
## outline(X), linear(x), line(O), LINE(O)
# text = 'outline linear line liNe lin LINE'
# mList = re.findall(r'\b(?i:line)\b', text)  # (?i) : 대소문자를 구분하지 않음
# print(mList)

## 3. 그룹 캡처
## 매칭된 결과 중에서 원하는 데이터를 가져오고 싶은 경우
## 날짜에서 년도, 월, 일 각각 얻기
# date = '2022-01-21'
# m = re.search(r'(\d{4})-(\d{2})-(\d{2})', date)
# if m != None:
#     print(m.group(0))
#     print(m.group(1))
#     print(m.group(2))
#     print(m.group(3))

## html 태그에서 원하는 정보 가져오기
# tr_tag = '<tr href="www.hello.com", id="abc123", class="ddd">hello</tr>'
## 클래스 속성값, 태그값 얻기
# m = re.search(r'.*class="(.*)">(.*)</tr>', tr_tag)
# print(m.group(1))
# print(m.group(2))

## 반복자를 통해서 탐색하는 경우
## Greedy 탐색(최대 매치), Non-Greedy 탐색(최소 매치)
## 기본 탐색은 Greedy 탐색
# m = re.search(r'\d{1,5}', '01066726345')
# print(m.group())

## Non-Greedy 탐색
## 반복자 뒤에 ? 삽입
# m = re.search(r'\d{3,5}?', '01066726345')
# print(m.group())

# li = '<li>나이키</li><li>아디다스</li><li>퓨마</li>'
# m = re.search(r'<li>(.*)</li>', li)
# print(m.group())
# print(m.group(1))
#
# m = re.search(r'<li>(.*?)</li>', li)
# print(m.group())
# print(m.group(1))

## 4. 그룹 캡처를 변수처럼 활용
## 그룹 1 : 전체 문자열
## 그룹 2 : 첫 글자
## 그룹 3 : 두번째 글자
## \그룹Number : 해당 그룹의 값을 활용  # \2는 2번째 그룹을 가리킴

# 총 3글자 중에 첫 글자와 마지막 글자가 같은 것과 매치
# mList = re.findall(r'((\w)(\w)\2)', 'abb 토마토 aba, XYXa 마토토')
# print(mList)
# mList = re.findall(r'((\w)(\w)\3)', 'abb 토마토 aba, XYXa 마토토')
# print(mList)

## 그룹 캡처를 안쓰고 싶은 경우
## ()로 문자들을 묶는 역할만 하고 싶은 경우
## (?:)로 표현
mList = re.findall(r'((?:abc)+)', 'abcabc abcabc abbbab abcabcabc')
print(mList)
mList = re.findall(r'((abc)+)', 'abcabc abcabc abbbab abcabcabc')
print(mList)
mList = re.findall(r'(abc)+', 'abcabc abcabc abbbab abcabcabc')
print(mList)
mList = re.findall(r'(abc+)', 'abcccccc abccab abcbac abbbab abcabcabc')
print(mList)

# ## split()
# ## 정규표현식에 매칭되는 것을 기준으로 문자열을 잘라 리스트로 반환
text = '14.5,1.2,10,2,300'
sList = re.split(r',', text)  # text.split(",")
text.split(",")

text = '14.5,     1.2,  10,  2,           300'
sList = re.split(r',\s*', text)
print(sList)

# ## sub()
## 정규표현식과 매칭되는 문자열을 다른 문자열로 바꿀 때 사용
## sub(정규표현식, 바꿀 문자값, 원본 문자열)
pNum = '811021-1234567'
# 주민번호의 마지막 7자리를 *로 바꾸기
subNum = re.sub(r'\d{7}', "*" * 7, pNum)
print(subNum)

# 그룹 캡처를 변수처럼 활용
subNum = re.sub(r'(\d{6})-\d{7}', '\g<1>-xxxxxxx', pNum)
print(subNum)
subNum = re.sub(r'(\d{6})-(\d{7})', 'xxxxxx-\g<2>', pNum)
print(subNum)
subNum = re.sub(r'(\d{6})-(\d{7})', '\g<2>-\g<1>', pNum)
print(subNum)

# 람다식 활용
# 매칭되는 문자 특수한 처리
text = 'apple 10, melon 50'
subStr = re.sub(r'\d+', lambda x: str(int(x.group()) + 2), text)
print(subStr)

# 모든 이름에 님 붙이기
names = '홍길동 임꺽정 김하나'
subName = re.sub(r'\w+', lambda x: x.group() + '님', names)
print(subName)