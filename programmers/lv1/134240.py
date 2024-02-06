# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 푸드 파이트 대회

def solution(food):
    answer = ""
    for i in range(1, len(food)):
        f = food[i]
        answer += str(i) * (f // 2)
    return answer + "0" + answer[::-1]
