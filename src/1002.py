import sys
import math

for _ in range(int(sys.stdin.readline())):
    count = 0
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    xx = (x1 - x2) ** 2
    yy = (y1 - y2) ** 2
    dis = float(math.sqrt(xx + yy))

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            count = -1
        else:
            count = 0
    elif dis > r1 + r2:
        count = 0
    elif dis + min(r1, r2) < max(r1, r2):
        count = 0
    elif abs(dis - (r1 + r2)) < 0.0000001:
        count = 1
    elif abs(dis - max(r1, r2) + min(r1, r2)) < 0.0000001:
        count = 1
    elif dis < r1 + r2:
        count = 2
    print(count)