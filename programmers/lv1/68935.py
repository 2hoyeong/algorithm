# https://programmers.co.kr/learn/courses/30/lessons/68935
# 월간 코드 챌린지 시즌1
# 3진법 뒤집기

def solution(n):
    digit = []
    while n > 0:
        digit.append(n % 3)
        n = n // 3
    answer = 0
    for i, num in enumerate(digit):
        answer += num * 3 ** (len(digit) - i - 1)
    return answer
