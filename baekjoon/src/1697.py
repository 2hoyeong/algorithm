from collections import deque

L = [0] * 100001
visited = [False] * 100001

N, K = map(int, input().split())

queue = deque()
queue.appendleft((N, 0))
while queue:
    now = queue.pop()
    if visited[now[0]] == True:
        continue
    visited[now[0]] = True
    if now[0] == K:
        print(now[1])
        break
    else:
        if now[0] >= 1:
            queue.appendleft((now[0] - 1, now[1] + 1))
        if now[0] < 100000:
            queue.appendleft((now[0] + 1, now[1] + 1))
        if now[0] <= 50000:
            queue.appendleft((now[0] * 2, now[1] + 1))
