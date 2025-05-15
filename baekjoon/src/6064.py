import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    answer = x
    lcmm = int(lcm(M, N)) + 1
    while answer <= lcmm:
        if (answer - 1) % N + 1 == y:
            break
        answer += M
    if answer >= lcmm:
        print(-1)
    else:
        print(answer)
