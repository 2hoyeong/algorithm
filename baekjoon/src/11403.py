import sys

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for g in graph:
    for e in g:
        print(e, end=' ')
    print()
