from collections import Counter

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
nums_counter = Counter(nums)

print(round(sum(nums) / N))
print(nums[N // 2])

freq = nums_counter.most_common(2)
if N == 1:
    print(freq[0][0])
else:
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])

print(nums[-1] - nums[0])
