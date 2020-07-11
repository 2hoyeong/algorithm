# https://programmers.co.kr/learn/courses/30/lessons/12900
# 2 x n 타일링

def solution(n):
    cases = [0, 1, 2]
    for i in range(2, n):
        cases.append((cases[i-1] + cases[i]) % 1000000007)
    return cases[n]