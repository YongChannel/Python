# 알파벳 찾기
import random
import time

alphabet = []
for i in range(26):
    alphabet.append(chr(ord('A') + i))

random.shuffle(alphabet)

randNum = random.randint(0, 26)
findCh = alphabet[randNum]

startTime = time.time()

while True:
    cnt = 0
    for ch in alphabet:
        if findCh != ch:
            print(ch, end=", ")
            cnt += 1
        if cnt % 10 == 0:
            print()
    print()

    isStr = input('입력: ')
    if isStr == findCh:
        endTime = time.time()
        print(f'정답 [{endTime - startTime:.1f}초]')
        break
    else:
        print('오답')
