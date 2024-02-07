# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    v_dungeons = permutations(dungeons, len(dungeons))
    for dungeons in v_dungeons:
        t = k
        d = 0
        for least, used in dungeons:
            if least > t:
                break
            t -= used
            d += 1
        answer = max(answer, d)
            
    return answer
