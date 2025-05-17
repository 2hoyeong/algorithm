import sys

N = int(sys.stdin.readline().rstrip())

graph = {}
for _ in range(N):
    nodes = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[nodes[0] - 1] = []
    for i in range(1, len(nodes), 2):
        if nodes[i] == -1:
            continue
        graph[nodes[0] - 1].append([nodes[i] - 1, nodes[i + 1]])

def find_maximum(start):
    costs = [0] * N
    visited = [False] * N
    queue = [start]
    
    while queue:
        now = queue.pop()

        if visited[now] == True:
            continue
        
        visited[now] = True

        for x, v in graph[now]:
            if visited[x] == False:
                costs[x] = costs[now] + v
                queue.append(x)

    return costs

costs = find_maximum(0)
max_node = costs.index(max(costs))

result = find_maximum(max_node)
print(max(result))
