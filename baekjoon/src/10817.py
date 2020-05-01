# 세 수
import sys

que = list(map(int, sys.stdin.readline().rstrip().split()))
que.sort()
print(que[1])