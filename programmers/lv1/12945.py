# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

def solution(n):
    answer = [1, 1]
    for i in range(2, n):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[n - 1] % 1234567