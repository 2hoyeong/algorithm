# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# 2018 KAKAO BLIND RECRUITMENT
# n진수 게임

def conv(n, b):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    while True:
        q, r = divmod(n, b)
        if q == 0:
            result += num[r]
            break
        else:
            result += num[r]
            n = q
    return result[::-1]

def solution(n, t, m, p):
    mapp = ''
    answer = ''
    for i in range(t * m):
        mapp += conv(i, n)
    
    for i in range(t):
        answer += mapp[i * m + p - 1]
    return answer
