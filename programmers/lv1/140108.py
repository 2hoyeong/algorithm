# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 문자열 나누기

def solution(s):
    answer = 0
    x = s[0]
    right = 1
    wrong = 0

    for i in range(1, len(s) - 1):
        c = s[i]
        if x == c:
            right += 1
        else:
            wrong += 1
        
        if right == wrong:
            answer += 1
            x = s[i + 1]
            right = 0
            wrong = 0
    return answer + 1
