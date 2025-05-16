import sys

N = int(input())

houses = []
for _ in range(N):
    houses.append(list(map(int, sys.stdin.readline().rstrip().split())))

if N < 2:
    print(min(houses[0]))
else:
    R = [houses[0][0]]
    G = [houses[0][1]]
    B = [houses[0][2]]

    for i in range(1, N):
        R.append(min(G[i - 1], B[i - 1]) + houses[i][0])
        G.append(min(R[i - 1], B[i - 1]) + houses[i][1])
        B.append(min(R[i - 1], G[i - 1]) + houses[i][2])


    print(min(R[-1], G[-1], B[-1]))
