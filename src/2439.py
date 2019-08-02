# 별 찍기 - 2

import sys

a = int(sys.stdin.readline()) + 1
for i in range(1, a):
    print((" " * (a - i - 1)) + "*"*i)