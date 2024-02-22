# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 롤케이크 자르기

def solution(topping):
    answer = 0
    h = {}
    d = {}
    for t in topping:
        if t in h:
            h[t] += 1
        else:
            h[t] = 1
    
    for t in topping:
        h[t] -= 1
        if h[t] == 0:
            del h[t]
        
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
        
        if len(h) == len(d):
            answer += 1
        
    
    return answer
