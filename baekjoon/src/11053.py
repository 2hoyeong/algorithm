N = int(input())
nums = list(map(int, input().split()))

dp = [1]
if N <= 1:
    print(1)
else:
    for i in range(1, N):
        dp.append(1)
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
