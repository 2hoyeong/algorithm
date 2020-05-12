# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버

answer = 0

def solution(numbers, target):
    def add(index, number):
        global answer
        if index > 0:
            add(index - 1, number + numbers[index - 1])
            add(index - 1, number - numbers[index - 1])
        else:
            if number == target:
                answer += 1
    add(len(numbers), 0)
    return answer