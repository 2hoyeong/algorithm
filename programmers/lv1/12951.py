# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

def solution(s):
    text = s.lower().split(" ")
    answer = ''
    for word in text:
        if word != "":
            answer += word[0].upper() + word[1:] + " "
        else:
            answer += " "
    return answer[:-1]