N = int(input())

triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

if N == 1:
    print(triangle[0][0])
else:
    for i in range(N - 1):
        for j in range(i + 1):
            if j == 0:
                triangle[i + 1][j] = triangle[i + 1][j] + triangle[i][j]
            else:
                triangle[i + 1][j] = max(triangle[i + 1][j] - triangle[i][j - 1] + triangle[i][j], triangle[i + 1][j])
            triangle[i + 1][j + 1] = triangle[i][j] + triangle[i + 1][j + 1]

    print(max(triangle[N - 1]))
