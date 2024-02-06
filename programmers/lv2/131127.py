# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 할인 행사

def solution(want, number, discount):
    answer = 0

    bucket = {}
    for i in range(len(want)):
        bucket[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        l = discount[i:i+10]
        r = {}
        for e in l:
            if e in r:
                r[e] += 1
            else:
                r[e] = 1
        
        exit = True
        for b in bucket:
            if b in r and r[b] == bucket[b]:
                exit = True
            else:
                exit = False
                break
                

        if exit:
            answer += 1
    
    return answer
