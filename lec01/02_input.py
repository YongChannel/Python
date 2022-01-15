# 1. print()
print('hello', end="")
print('world')
print('hello', 'world', 'yong', sep='&')


# 2. format()
name, age, height = 'yong', 20, 180.5
print('%s %d %f' %(name, age, height))
print('%10s %10d %10.3f' %(name, age, height))
print('%-10s %-10d %-10.3f' %(name, age, height))

print('{} {} {}'.format(name, age, height))
print('{2} {0} {1}'.format(name, age, height))

print('{0:10} {1:5} {2:10.2f}'.format(name, age, height))
print('{0:^10} {1:^5} {2:^10.2f}'.format(name, age, height))
print('{0:-^10} {1:2^5} {2:a^10.2f}'.format(name, age, height))

print(f'{name} {age} {height}')


# 3. input()
num1 = int(input())
str1 = input()
print(f'{int(str1) + 5}')
print(f'{str(num1) + str(5)}')

name = list(map(int, input().split()))
print(f'{name}', type(name), type(name[0]))

name = list(map(str, input().split()))
print(f'{name}', type(name), type(name[0]))

name = list(map(float, input().split()))
print(f'{name}', type(name), type(name[0]))
