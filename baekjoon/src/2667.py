N = int(input())

field = [[0] * (N) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]

for i in range(N):
    apt = input()
    for j in range(len(apt)):
        field[i][j] = int(apt[j])

total_apt = 0
apts = []

def find(x, y):
    if x < 0 or y < 0 or x > N - 1 or y > N - 1:
        return 0
    if field[x][y] == 0 or visited[x][y] == True:
        return 0
    
    visited[x][y] = True
    return 1 + find(x - 1, y) + find(x + 1, y) + find(x, y - 1) + find(x, y + 1)

for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and visited[i][j] == False:
            total_apt += 1
            apts.append(find(i, j))

print(total_apt)
for apt in sorted(apts):
    print(apt)
