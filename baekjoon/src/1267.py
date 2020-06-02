# https://www.acmicpc.net/problem/1267
# 핸드폰 요금

import sys

N = int(sys.stdin.readline())
Ym, Mm = 0, 0
ms = map(int, sys.stdin.readline().split())
for m in ms:
    Ym += m // 30 * 10 + 10
    Mm += m // 60 * 15 + 15
    
if Ym < Mm:
    print("Y %d" % Ym)
elif Ym > Mm:
    print("M %d" % Mm)
else:
    print("Y M %d" % Ym)
