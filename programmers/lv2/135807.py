# https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 숫자 카드 나누기

import math

def gcd_N(arr):
    gcd = arr[0]
    for e in arr:
        gcd = math.gcd(gcd, e)
    return gcd

def solution(arrayA, arrayB):
    gcd1 = gcd_N(arrayA)
    gcd2 = gcd_N(arrayB)
    answer1, answer2 = 0, 0
    if gcd1 > 1:
        answer1 = gcd1
        for e in arrayB:
            if e % gcd1 == 0:
                answer1 = 0
                break
    if gcd2 > 1:
        answer2 = gcd2
        for e in arrayA:
            if e % gcd2 == 0:
                answer2 = 0
                break

    return max(answer1, answer2, 0)
