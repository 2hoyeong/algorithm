N, M = map(int, input().split())

graph = {}
visited = [False] * (N + 1)
for i in range(N + 1):
    graph[i] = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

answer = 0
for i in range(1, N + 1):
    if visited[i] == False:
      answer += 1
      stack = [i]
      while stack:
          n = stack.pop()
          if visited[n] == False:
              visited[n] = True
              nodes = graph[n]
              for node in nodes:
                  if visited[node] == False:
                      stack.append(node)

print(answer)
