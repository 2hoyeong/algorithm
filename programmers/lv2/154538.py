# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 숫자 변환하기

def solution(x, y, n):
    if x == y:
        return 0
    
    a = [9999999] * (y + 1)
    a[x] = 0
    
    for i in range(x, y + 1):
        if a[i] == 9999999:
            continue

        if i + n <= y:
            a[i + n] = min(a[i + n], a[i] + 1)

        if i * 2 <= y:
            a[i * 2] = min(a[i * 2], a[i] + 1)

        if i * 3 <= y:
            a[i * 3] = min(a[i * 3], a[i] + 1)
            
    if a[y] == 9999999:
        return -1
    
    return a[y]
