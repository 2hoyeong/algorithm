from collections import deque

N, M = map(int, input().split())

ladder = {}

for _ in range(N):
    start, end = map(int, input().split())
    ladder[start - 1] = end - 1

for _ in range(M):
    start, end = map(int, input().split())
    ladder[start - 1] = end - 1

visited = [False] * 100

queue = deque()
queue.append((0, 0))

while queue:
    now, roll = queue.pop()

    if visited[now] == True:
        continue
  
    if now == 99:
        print(roll)
        break

    visited[now] = True

    if now in ladder:
        visited[now] = False
        queue.append((ladder[now], roll))
    else:
        for i in range(1, 7):
            if now + i <= 99:
                queue.appendleft((now + i, roll + 1))
