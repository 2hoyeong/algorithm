# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최소공배수

def solution(n, m):
    lcm = n * m
    while m != 0:
        d = n % m
        n, m = m, d
    return [n, lcm / n]