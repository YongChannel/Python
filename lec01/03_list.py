# 1. 리스트
nums = [1, 2, 3, 4, 5]
newNums = [1, 3, 2, 4, 5]
colors1 = ['red', 'yellow', 'green', 'blue']
colors2 = ['white', 'black']
tempList = ['red', 1, 3.14, [1, 3.12, 'blue']]

print(len(nums), sum(nums))
print(colors1 + colors2, nums * 2)
print(3 in nums, 'red' in colors1, 'white' in colors1)
print(tempList, len(tempList[3]), tempList[-1][2])


# 2. 슬라이싱
print(nums[:3], nums[2:], nums[1:4])
print(nums[4::-2])
print(nums[-1:-4:-1])


# 3. 리스트 요소 언패킹
n1, n2, n3, n4, n5 = nums
c1, c2, c3, c4 = colors1
print(n1, n2, n3, n4, n5, c1, c2, c3, c4)


# 4. 리스트 메소드
# append()
nums.append(99)
print(nums)

# insert()
nums.insert(0, 99)
print(nums)

# remove()
nums.remove(99)
print(nums)

# del
del colors1[0]
print(colors1)

# pop()
print(colors1.pop(), colors2.pop(1))
print(colors1, colors2)

# sort()
newNums.sort()
print(newNums)
newNums.sort(reverse=True)
print(newNums)

# sorted()
tempNums = sorted(newNums)
print(tempNums, newNums)

tempNums = sorted(newNums, reverse=True)
print(tempNums)

# count()
print(nums.count(2), nums.count('red'))
