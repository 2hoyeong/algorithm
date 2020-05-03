# https://programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팁스타운
# 짝지어 제거하기
# https://velog.io/@dramatic/Algorithm-%EC%A7%9D%EC%A7%80%EC%96%B4-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0

def solution(s):
    s = list(s)
    answer = []
    
    for c in s:
        if [c] == answer[-1:]:
            answer.pop()
        else:
            answer.append(c)

    return not(answer)