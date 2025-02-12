from collections import deque

N, M, V = map(int, input().split())

graph = {}

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

stack = deque()
q = deque()

    
dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

dfs_answer = []

stack.append(V)
while len(stack) > 0:
    current_node = stack.pop()
    if dfs_visited[current_node] == False:
        dfs_visited[current_node] = True
        dfs_answer.append(str(current_node))
        next_nodes = graph[current_node]
        for node in sorted(next_nodes, reverse=True):
            if dfs_visited[node] == False:
                stack.append(node)

bfs_answer = []

q.append(V)
while len(q) > 0:
    current_node = q.pop()
    if bfs_visited[current_node] == False:
        bfs_visited[current_node] = True
        bfs_answer.append(str(current_node))
        next_nodes = graph[current_node]
        for node in sorted(next_nodes):
            if bfs_visited[node] == False:
                q.appendleft(node)

print(' '.join(dfs_answer))
print(' '.join(bfs_answer))
