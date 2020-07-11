# https://programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크

def solution(n, computers):
    visited = [x + 1 for x in range(n)]
    bfs = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1 and visited[j] == j + 1:
                visited[j] = visited[i]
                bfs.append(j)
            while bfs:
                start = bfs.pop()
                for dest in range(n):
                    if start == dest:
                        continue
                    if computers[start][dest] == 1 and visited[dest] == dest + 1:
                        bfs.append(dest)
                        visited[dest] = visited[start]
    return len(set(visited))