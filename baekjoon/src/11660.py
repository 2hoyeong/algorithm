import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

board = []
acc = []
for i in range(N):
    acc.append([])
    for e in map(int, sys.stdin.readline().rstrip().split()):
        if len(acc[i]) == 0:
            acc[i].append(e)
        else:
            acc[i].append(acc[i][-1] + e)
        board.append(e)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    result = 0
    for i in range(x1 - 1, x2):
        if y1 - 2 < 0:
            result += acc[i][y2 - 1]
        else:
            result += acc[i][y2 - 1] - acc[i][y1 - 2]
    print(result)
