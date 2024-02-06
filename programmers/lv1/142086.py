# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 가장 가까운 같은 글자

def solution(s):
    answer = []
    which = {}
    for i in range(len(s)):
        c = s[i]
        if c in which:
            answer.append(i - which[c])
        else:
            answer.append(-1)
        which[c] = i
    return answer
