T = int(input())

for _ in range(T):
    N = int(input())
    triangle = [1, 1, 1]
    for i in range(3, N):
        triangle.append(triangle[i - 2] + triangle[i - 3])
    print(triangle[N - 1])
