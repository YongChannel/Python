# 1. 문자열
str1 = 'hello'
str2 = 'world'
str3 = 'YONG'
str4 = '     hello-----'
str5 = '1, 2, 3, 4, 5'
str6 = ['a', 'b', 'c', 'd']

print(str1 + str2, str1 * 2)
print('h' in str1, 'h' in str2)
print(str1[0], str1[-1], str1[:3])

# count()
print(str1.count('h'), str2.count('h'))

# find()
print(str1.find('h'), str2.find('d'), str2.find('e'))

# upper() / lower()
print(str1.upper(), str3.lower())
name = 'yongchan'
print(name[0].upper() + name[1:])

# 2. 공백 제거
print(str4.strip())
print(str4.lstrip(), str4.rstrip('-'))

# 3. 문자열 고체
print(str4.replace('-----', ' yong'))

# 4. 리스트 변환
print(list(str4))
print(str4.split())
print(str5.split(','))

# 5. join()
print('-'. join(str6))
