# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기

def solution(number, k):
    answer = []
    number = list(str(number))
    answer.append(number[0])
    for i in range(1, len(number)):
        if k > 0:
            if [number[i]] > answer[-1:]:
                while k and answer and [number[i]] > answer[-1:]:
                    answer.pop()
                    k -= 1
            answer.append(number[i])
        else:
            answer.append(number[i])
    answer = answer[:len(answer) - k]
    return ''.join(answer)
