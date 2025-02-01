N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.reverse()

result = 0
for coin in coins:
    if K < coin:
        continue
    count = K // coin
    result += count
    K -= count * coin

print(result)
