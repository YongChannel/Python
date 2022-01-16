# 달력 만들기
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f'{i:0>2} : {j:0>2} : {k:0>2}')

# test
# 01 02 03 04 05
# 06 ...
# 11 ...
# 16 17 18 19 20

for i in range(1, 21):
    print(f'{i:0>2}', end='')
    if i % 5 != 0:
        print(f'', end=', ')
    if i % 5 == 0:
        print()

# 01 02 03 04 05
# 10 ...
# 11 ...
# 20 19 18 17 16

row, col = map(int, input().split())
for i in range(row):
    if i % 2 == 0:
        for j in range(col):
            print(f'{i * col + 1 + j:0>2}', end=' ')
    else:
        for k in range(col - 1, -1, -1):
            print(f'{i * col + 1 + k:0>2}', end=' ')
    print()
