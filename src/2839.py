# 설탕 배달
import sys

N = int(sys.stdin.readline())
bag = [0, 0]

while N >= 3:
    if N % 15 == 0:
        N -= 15
        bag[1] += 3
    elif N % 3 != 0:
        N -= 5
        bag[1] += 1
    else:
        N -= 3
        bag[0] += 1

if N is not 0:
    print("-1")
else:
    print(bag[0] + bag[1])