# https://www.acmicpc.net/problem/10866
# 덱

from collections import deque
import sys

class teque(deque):
    def __init__(self):
        super()
        self.size = 0

    def append(self, data):
        super().append(data)
        self.size += 1

    def appendleft(self, data):
        super().appendleft(data)
        self.size += 1
    def popleft(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return super().popleft()

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return super().pop()

    def getsize(self):
        return self.size


    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self[-1]
            

d = teque()
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push_front":
        d.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        d.append(cmd[1])
    elif cmd[0] == "pop_front":
        print(d.popleft())
    elif cmd[0] == "pop_back":
        print(d.pop())
    elif cmd[0] == "size":
        print(d.getsize())
    elif cmd[0] == "empty":
        print(d.empty())
    elif cmd[0] == "front":
        print(d.front())
    elif cmd[0] == "back":
        print(d.back())

