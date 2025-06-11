import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

chickens = []
houses = []

for i in range(N):
    board = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        e = board[j]
        if e == 1:
            houses.append([i, j])
        elif e == 2:
            chickens.append([i, j])


visited = [False] * len(chickens)

answer = 2500

def dfs(idx, depth):
    global answer, visited

    if depth == M:
        distances = 0

        for house in houses:
            x, y = house
            distance = 2500

            for i in range(len(chickens)):
                if visited[i]:
                    distance = min(distance, abs(x - chickens[i][0]) + abs(y - chickens[i][1]))
            distances += distance
        
        answer = min(answer, distances)

    else:
        for i in range(idx, len(chickens)):
            if not visited[i]:
                visited[i] = True
                dfs(i + 1, depth + 1)
                visited[i] = False

dfs(0, 0)
print(answer)
