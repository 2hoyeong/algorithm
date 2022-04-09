# https://programmers.co.kr/learn/courses/30/lessons/87389
# 월간 코드 챌린지 시즌3
# 나머지가 1이 되는 수 찾기

def solution(n):
    a = [False, False] + [True]*(1000000-1)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    for p in primes:
        if n % p == 1:
            return p
    return n - 1
