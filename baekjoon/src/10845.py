from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
    op = input().split()

    if op[0] == 'push':
        queue.appendleft(op[1])
    elif op[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            v = queue.pop()
            print(v)
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif op[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
