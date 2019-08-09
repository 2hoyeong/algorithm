# 소수 찾기

N = int(input())
C = map(int, input().split())

count = 0
for n in C:
    if n == 1:
        continue

    if n >= 4:
        if not n % 2 or not n % 3:
            continue

    BOOL = True
    for i in range(4, n - 1):
        if n % i == 0:
            BOOL = False
            break

    if BOOL:
        count += 1

print(count)