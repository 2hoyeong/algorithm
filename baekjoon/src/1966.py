TC = int(input())

for _ in range(TC):
    N, D = map(int, input().split())

    P = list(map(int, input().split()))
    lp = len(P)
    exit_condition = [-1] * lp
    q = [0] * lp
    count = 1
    cursor = 0
    while True:
        if P == exit_condition:
            break
        
        priority = max(P)
        if P[cursor] == priority:
            q[cursor] = count
            P[cursor] = -1
            count += 1
        else:
            cursor = (cursor + 1) % lp

    print(q[D])
