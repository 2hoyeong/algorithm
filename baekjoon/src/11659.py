import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

acc = [0] * (N + 1)
nums = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, len(nums) + 1):
    acc[i] = acc[i - 1] + nums[i - 1]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(acc[end] - acc[start - 1])
