# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기
# Summer/Winter Coding(~2018)

import itertools

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    nums = list(itertools.combinations(nums, 3))
    for num in nums:
        number = sum(num)
        if isPrime(number):
            answer += 1
    return answer