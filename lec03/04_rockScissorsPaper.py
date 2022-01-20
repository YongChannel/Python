import random

winTable = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}

messages = {
    'win': '이겼다',
    'draw': '비겼다',
    'lose': '졌다'
}

rcpCum = ['가위', '바위', '보']


def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif winTable[mine] == yours:
        return 'win'
    else:
        return 'lose'


while True:
    random.shuffle(rcpCum)
    comStr = rcpCum[0]
    userStr = input('가위 / 바위 / 보 => ')

    if userStr == '끝':
        print('[종료]')
        break
    elif userStr not in rcpCum:
        print('[다시]')
        continue

    data = rsp(userStr, comStr)
    print(data)
    print(messages[data])
