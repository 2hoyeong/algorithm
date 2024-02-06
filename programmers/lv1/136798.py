# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 기사단원의 무기

def solution(number, limit, power):
    answer = 0
    for nn in range(1, number + 1):
        n = gd(nn)
        if n > limit:
            answer += power
        else:
            answer += n
    return answer

def gd(n):
    d = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            d += 1
            if ( (i**2) != n) : 
                d += 1
    return d
