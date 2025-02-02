N = int(input())
E = int(input())

visited = [False] * (N + 1)
graph = {1: []}

for _ in range(E):
    start, end = map(int, input().split())
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

def find(n):
    visited[n] = True
    nodes = graph[n]
    for node in nodes:
        if not visited[node]:
            find(node)
                
find(1)
print(sum(visited) - 1)
