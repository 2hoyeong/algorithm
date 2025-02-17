from collections import deque

T = int(input())

def d(n):
    return (2 * n) % 10000

def s(n):
    if n == 0:
        return 9999
    else:
        return n - 1

def l(n):
    a = n % 1000
    b = n // 1000
    return a * 10 + b

def r(n):
    a = n % 10
    b = n // 10
    return a * 1000 + b

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.appendleft((A, ''))
    while queue:
        now = queue.pop()
        if visited[now[0]] == True:
            continue
        visited[now[0]] = True

        result_d = d(now[0])
        if result_d == B:
            print(now[1] + 'D')
            break
        else:
            queue.appendleft((result_d, now[1] + 'D'))

        result_s = s(now[0])
        if result_s == B:
            print(now[1] + 'S')
            break
        else:
            queue.appendleft((result_s, now[1] + 'S'))
        
        result_l = l(now[0])
        if result_l == B:
            print(now[1] + 'L')
            break
        else:
            queue.appendleft((result_l, now[1] + 'L'))
        
        result_r = r(now[0])
        if result_r == B:
            print(now[1] + 'R')
            break
        else:
            queue.appendleft((result_r, now[1] + 'R'))
