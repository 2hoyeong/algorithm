# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 연습문제
# 뒤에 있는 큰 수 찾기

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        n = numbers[i]
        while stack and numbers[stack[-1]] < n:
            answer[stack[-1]] = n
            stack.pop()

        stack.append(i)

    return answer
