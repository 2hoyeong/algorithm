# https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 연속된 부분 수열의 합

def solution(sequence, k):
    answer = []
    p1, p2 = 0, 0
    point_sum = sequence[0]
    while True:
        if point_sum == k:
            if not answer:
                answer = [[p1, p2]]
            if p1 == p2:
                return [p1, p2]
            else:
                if p2 - p1 < answer[0][1] - answer[0][0]:
                    answer = [[p1, p2]]
        
        if point_sum >= k:
            point_sum -= sequence[p1]
            p1 += 1
        else:
            p2 += 1
            if p2 >= len(sequence):
                break
            point_sum += sequence[p2]
    return answer[0]
