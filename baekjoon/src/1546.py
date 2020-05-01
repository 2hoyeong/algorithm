# 평균

import sys

T = int(sys.stdin.readline().rstrip())
I = map(int, sys.stdin.readline().rstrip().split())
L = list()

for i in I:
    L.append(i)

M = max(L)
R = list()
for l in L:
    R.append(l / M * 100)

print(sum(R) / len(R))