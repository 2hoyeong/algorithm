N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    apt = [[x for x in range(1, n + 1)]]

    for i in range(1, k + 1):
        apt.append([0] * n)
        apt[i][0] = apt[i - 1][0]
        for j in range(1, n):
            apt[i][j] = apt[i][j - 1] + apt[i - 1][j]
    
    print(apt[k][n - 1])
