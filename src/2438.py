# 별 찍기 - 1

import sys

stars = int(sys.stdin.readline()) + 1
for l in range(1, stars):
    print("*" * l)