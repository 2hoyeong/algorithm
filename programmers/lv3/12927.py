# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 야근 지수

import heapq

def solution(n, works):
    hq = []
    for w in works:
        heapq.heappush(hq, (-w, w))
    
    for _ in range(n):
        if len(hq) == 0:
            return 0
        _ ,w = heapq.heappop(hq)
        w -= 1
        if w > 0:
            heapq.heappush(hq, (-w, w))
            
    return sum([x * x for _, x in hq])
