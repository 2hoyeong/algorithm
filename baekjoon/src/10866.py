# https://www.acmicpc.net/problem/10866
# 덱

import sys

class deque():
    def __init__(self):
        self.datas = []
        self.size = 0

    def appendleft(self, data):
        self.datas.insert(0, data)
        self.size += 1

    def append(self, data):
        self.datas.append(data)
        self.size += 1
    def popleft(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.datas.pop(0)

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.datas.pop()

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
            return self.datas[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.datas[-1]
            

d = deque()
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
