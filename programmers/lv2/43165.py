# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버
# https://velog.io/@dramatic/Algorithm-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84

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