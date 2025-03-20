from collections import deque

A, B = map(int, input().split())

result = -1
queue = deque()
queue.appendleft((A * 2, 1))
queue.appendleft((A * 10 + 1, 1))

while queue:
    now, depth = queue.pop()

    if now == B:
        result = depth + 1
        break
    
    if now < B:
        queue.appendleft((now * 2, depth + 1))
        queue.appendleft((now * 10 + 1, depth + 1))

print(result)
