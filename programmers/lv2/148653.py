# https://school.programmers.co.kr/learn/courses/30/lessons/148653
# 마법의 엘리베이터

def solution(storey):
    answer = 0
    while storey > 0:
        if storey % 10 == 0:
            storey //= 10
            continue
        
        if storey % 10 >= 6:
            storey += 1
        
        elif storey % 10 == 5 and (storey // 10) % 10 >= 5:
            storey += 1
        else:
            storey -= 1

        answer += 1

    return answer
