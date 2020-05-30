# https://www.acmicpc.net/problem/18258
# 큐 2

import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()
size = 0
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    print(que)
    if cmd[0] == "push":
        que.append(cmd[1])
        size += 1
    elif cmd[0] == "pop":
        if que:
            print(que.popleft())
            size -= 1
        else:
            print(-1)
    elif cmd[0] == "size":
        print(size)
    elif cmd[0] == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if size == 0:
            print(-1)
        else:
            print(que[0])
    elif cmd[0] == "back":
        if size == 0:
            print(-1)
        else:
            print(que[-1])
