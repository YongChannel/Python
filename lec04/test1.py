# 곱셈표
start = 2
while start != 11:
    for j in range(1, 4):
        for i in range(start, start + 3):
            if i == 10:
                break
            if i * j >= 10:
                print(f"{i} x {j} = {i * j:<5}", end='')
            else:
                print(f"{i} x {j} = {i * j:<5}", end='')
        print()
    print()
    start += 3

for i in range(2, 9, 3):
    for j in range(1, 4):
        if i != 8:
            print(f'{i} x {j} = {i * j:<10}', end='')
            print(f'{i + 1} x {j} = {(i + 1) * j:<10}', end='')
            print(f'{i + 2} x {j} = {(i + 2) * j:<10}')
        else:
            print(f'{i} x {j} = {i * j:<10}', end='')
            print(f'{i + 1} x {j} = {(i + 1) * j:<10}')
    print()

count = 0
for i in [1, 2, 3] * 3:
    for j in [2, 3, 4]:
        if count == 0:
            result = str(j) + 'X' + str(i) + '=' + str(j * i)
            print(f'{result:<15}', end='')
            if i == 3 and j == 4:
                count += 1
                print()
        elif count == 1:
            result = str(j + 3) + 'X' + str(i) + '=' + str((j + 3) * i)
            print(f'{result:<15}', end='')
            if i == 3 and j == 4:
                count += 1
                print()
        elif count == 2:
            if j != 4:
                result = str(j + 6) + 'X' + str(i) + '=' + str((j + 6) * i)
                print(f'{result:<15}', end='')
    print()

iter_a = [1, 2, 3] * 3
iter_b = ([2] * 3) + ([5] * 3) + ([8] * 3)

for idx, (i, j) in enumerate(zip(iter_a, iter_b)):
    a = 2 if idx > 5 else 3

    for n in range(a):
        result = str(j + n) + 'X' + str(i) + '=' + str((j + n) * i)
        print(f'{result:<15}', end='')

    print()
    if (idx + 1) % 3 == 0:
        print()

lastDan = 9
lastNum = 3
numOfLine = 3
for i in range(2, lastDan + 1, numOfLine):
    for j in range(1, lastNum + 1):
        for k in range(numOfLine):
            if i + k <= lastDan:
                print(f'{i + k} x {j} = {(i + k) * j:<6}', end='')
        print()
    print()


def printer(a, b):
    for i in range(1, 4):
        for j in range(a, b):
            print(f'{j} x {i} = {i * j:<10}', end="")
        print()
    print()


printer(2, 5)
printer(5, 8)
printer(8, 10)

# 로또 문제
import random

lotNum = []
for i in range(6):
    randNum = random.randint(1, 46)
    while randNum in lotNum:
        randNum = random.randint(1, 46)
    lotNum.append(randNum)

print(f'나의 번호 입력: ', end="")
myNum = list(map(int, input().split()))
collNum = [i for i in lotNum for j in myNum if i == j]

print(f'당첨 번호: {lotNum}')
print(f'나의 번호: {myNum}')
print(f'맞춘 번호: {collNum}')
print(f'맞춘 개수: {len(collNum)}')
