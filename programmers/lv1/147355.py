# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 크기가 작은 부분 문자열

def solution(t, p):
    answer = 0
    tl = len(t)
    pl = len(p)
    left = 0
    right = pl
    pi = int(p)
    while tl >= right:
        target = int(t[left:right])
        if pi >= target:
            answer += 1
        left += 1
        right += 1
    return answer
