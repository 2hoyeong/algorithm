# https://www.acmicpc.net/problem/4948
# 베르트랑 공준

import sys

pn = [True] * (123456 * 2 + 1)
m = int((123456 * 2 + 1) ** 0.5)
for i in range(2, m + 1):
    if pn[i] == True:
        for j in range(i + i, (123456 * 2 + 1), i):
            pn[j] = False

while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    print(len([i for i in range(N + 1, N + N + 1) if pn[i] == True]))