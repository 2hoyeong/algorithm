import sys
N = int(sys.stdin.readline().rstrip())

nums = {}
last = 0
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

    if num > last:
        last = num

for i in range(last + 1):
    if i in nums:
        for _ in range(nums[i]):
            print(i)
