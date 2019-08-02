# 문자열 반복

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split(' ', 1)

    for c in S:
        for _ in range(int(R)):
            print(c, end='')

    print()