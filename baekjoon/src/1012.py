T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0]*(N) for _ in range(M)]
    visited = [[False]*(N) for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    def dfs(x, y):
        if x < 0 or y < 0:
            return 0
        if x >= M or y >= N:
            return 0
        if field[x][y] != 1 or visited[x][y] != False:
            return 0
        
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    answer = 0
    for n in range(N):
        for m in range(M):
            if field[m][n] == 1 and visited[m][n] == False:
                dfs(m, n)
                answer += 1

    print(answer)
