from collections import deque
N, M = map(int, input().split())

friends = {}

for i in range(N + 1):
  friends[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

kb = []

for i in range(1, N + 1):
    per = []
    visited = [False] * (N + 1)
    queue = deque()
    queue.append((i, 0))
    while queue:
        now, depth = queue.pop()

        if visited[now] == True:
            continue
        
        visited[now] = True
        per.append(depth)
        for friend in friends[now]:
            queue.appendleft((friend, depth + 1))
    
    kb.append(sum(per))

print(kb.index(min(kb)) + 1)
