# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq

def solution(scoville, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    answer = 0
    while h[0] < K:
        if len(h) > 1:
            f = heapq.heappop(h)
            s = heapq.heappop(h)
            heapq.heappush(h, f + (s * 2))
            answer += 1
        else:
            return -1
    return answer