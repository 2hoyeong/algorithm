import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

graph = [[100001] * (N) for _ in range(N)]

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start - 1][end - 1] = min(cost, graph[start - 1][end - 1])

f, t = map(int, sys.stdin.readline().rstrip().split())
heap = [1000 * 100000] * N
heap[f - 1] = 0
q = deque()
q.append(f - 1)

while q:
    i = q.pop()
    for j in range(N):
        if graph[i][j] == 100001:
            continue
        if heap[j] > heap[i] + graph[i][j]:    
            heap[j] = heap[i] + graph[i][j]
            q.appendleft(j)
print(heap[t - 1])
