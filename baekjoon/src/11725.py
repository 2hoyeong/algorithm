import sys
from collections import deque

N = int(input())
graph = { 1: [] }

for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]
    
    if B in graph:
        graph[B].append(A)
    else:
        graph[B] = [A]

queue = deque()
queue.append(1)

visited = [False] * (N + 1)
parent = [0] * (N + 1)

while queue:
    now = queue.pop()
    if visited[now] == True:
        continue
    
    visited[now] = True

    for child in graph[now]:
        if visited[child] == False:
            parent[child] = now
            queue.append(child)

for i in range(2, N + 1):
    print(parent[i])
