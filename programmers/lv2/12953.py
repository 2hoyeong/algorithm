# https://programmers.co.kr/learn/courses/30/lessons/12953
# 연습문제
# N개의 최소공배수

def solution(arr):
    while len(arr) > 1:
        a, b = arr[:2]
        arr = arr[2:]
        n = int(lcm(a, b))
        arr.append(n)
        
    return arr[0]

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b / gcd(a,b);

