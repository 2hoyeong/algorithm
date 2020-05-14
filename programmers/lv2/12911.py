# https://programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

def solution(n):
    i = n
    n = bin(n).count("1")
    while True:
        i += 1
        if n == bin(i).count("1"):
            return i