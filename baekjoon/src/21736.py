import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

campus = []
visisted = [[False] * M for _ in range(N)]

start = [0, 0]

for i in range(N):
    c = list(sys.stdin.readline().rstrip())
    try:
        j = c.index("I")
        start = [i, j]
    except:
        pass
    campus.append(c)

stack = []
stack.append(start)
result = 0

while stack:
    x, y = stack.pop()
    
    if visisted[x][y] == True:
        continue
    
    if campus[x][y] == "X":
        continue
    
    visisted[x][y] = True
    if campus[x][y] == "P":
      result += 1
    
    if x - 1 >= 0:
        stack.append([x - 1, y])
    if x + 1 < N:
        stack.append([x + 1, y])
    if y - 1 >= 0:
        stack.append([x, y - 1])
    if y + 1 < M:
        stack.append([x, y + 1])

if result == 0:
    print("TT")
else:
    print(result)
