import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dp = [[0] * N for _ in range(3)]
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().rstrip().split())))

    if N == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp[0][1] = stickers[0][1] + stickers[1][0];
    dp[1][1] = stickers[1][1] + stickers[0][0];
    dp[2][1] = max(stickers[0][0], stickers[1][0])
    for i in range(2, N):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2], dp[2][i - 1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2], dp[2][i - 1]) + stickers[1][i]
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1])

    print(max(dp[0][-1], dp[1][-1], dp[2][-1]))
