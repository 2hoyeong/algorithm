# https://school.programmers.co.kr/learn/courses/30/lessons/340212
# PCCP 기출문제
# 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = 10**15

    while left <= right:
        level = (left + right) // 2
        time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            if diff > level:
                time += (diff - level + 1) * times[i]
                if i > 0:
                    time += (diff - level) * times[i - 1]
            else:
                time += times[i]

        if time > limit:
            left = level + 1
        else:
            answer = level
            right = level - 1


    return answer
