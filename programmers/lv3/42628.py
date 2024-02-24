# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐

import heapq

def solution(operations):
    maxq = []
    minq = []
    for op in operations:
        if op == "D 1" and len(maxq) > 0:
            heapq.heappop(maxq)
            if len(maxq) <= 1:
                minq = maxq.copy()
        elif op == "D -1" and len(minq) > 0:
            heapq.heappop(minq)
            if len(minq) <= 1:
                maxq = minq.copy()
        elif op[0] == "I":
            num = int(op[2:])
            heapq.heappush(minq, (num, num))
            heapq.heappush(maxq, (-num, num))
        
    if len(maxq) == 0 or len(minq) == 0:
        return [0, 0]
    
    return [maxq[0][1], minq[0][1]]
