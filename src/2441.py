# 별 찍기 - 4

import sys

a = int(sys.stdin.readline())
for i in range(1, (a + 1)):
    print(" "*(i - 1) + "*"*(a + 1 - i))