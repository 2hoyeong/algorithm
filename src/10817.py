# 세 수
import sys

que = [0, 0, 0]
A, B, C = map(int, sys.stdin.readline().rstrip().split())
que[0] = A
if que[0] > B:
    que[1] = B
else:
    que[0] = B
    que[1] = A

if que[0] > C:
    if que[1] > C:
        que[2] = C
    else:
        que[2] = que[1]
        que[1] = C
else:
    que[2] = que[1]
    que[1] = que[0]
    que[0] = C

print(que[1])