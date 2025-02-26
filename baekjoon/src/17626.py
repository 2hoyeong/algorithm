import sys

n = int(sys.stdin.readline().rstrip())

if int(n ** 0.5) ** 2 == n:
    print(1)
else:
    dp = [0, 1]

    for i in range(2, n + 1):
        minimum = 4
        for j in range(int(i ** 0.5), 0, -1):
            minimum = min(minimum, dp[i - j ** 2] + 1)
        dp.append(minimum)

    print(dp[n])
