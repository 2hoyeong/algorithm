N = int(input())
P = list(map(int, input().split()))

P.sort()
acc = 0
result = 0
for p in P:
    result += p + acc
    acc += p

print(result)
