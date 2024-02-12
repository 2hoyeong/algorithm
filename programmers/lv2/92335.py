# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 2022 KAKAO BLIND RECRUITMENT
# k진수에서 소수 개수 구하기

import math

def is_prime_number(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def conv(n, b):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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

def solution(n, k):
    answer = 0
    N = conv(n, k)
    x = N.split("0")
    x = list(filter(lambda x: x != "", x))
    while len(x) > 0:
        e = x.pop()
        isPrime = is_prime_number(int(e))
        if isPrime:
            answer += 1
            
    return answer
