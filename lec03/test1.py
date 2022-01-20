# 별찍기
# 1
for i in range(1, 11):
    print('*' * i)

# 2
for i in range(1, 11):
    print(' ' * (10 - i) + '*' * i)

# 3
for i in range(1, 20, 2):
    print(f"{('*' * i):^20}")
for i in range(1, 11):
    print(' ' * (10 - i) + '*' * (2 * i - 1))

# 4
for i in range(1, 11):
    print(' ' * (10 - i) + '*' * (2 * i - 1))
for i in range(9, 0, -1):
    print(' ' * (10 - i) + '*' * (2 * i - 1))

star = ['*' * i for i in range(1, 20, 2)]
result = star + star[-2::-1]

for i in result:
    print(f"{i:^19}")


# 3, 6, 9
for i in range(1, 51):
    numStr = str(i)
    cnt = numStr.count('3') + numStr.count('6') + numStr.count('9')
    if cnt > 0:
        print('짝' * cnt, end="")
    else:
        print(numStr, end="")
    if i != 50:
        print(end=", ")