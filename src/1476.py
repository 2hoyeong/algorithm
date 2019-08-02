# 날짜 계산

import sys

E, S, M = map(int, sys.stdin.readline().rstrip().split())
year = 1
while True:
    if E == 1 and S == 1 and M == 1:
        break
    E -= 1
    S -= 1
    M -= 1
    if not E:
        E += 15
    if not S:
        S += 28
    if not M:
        M += 19
    year += 1

print(year)