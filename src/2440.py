# 별 찍기 - 3

import sys

a = int(sys.stdin.readline())
for i in range(1, (a + 1)):
    print("*"*(a + 1 - i))