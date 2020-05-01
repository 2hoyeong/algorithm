# https://programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 내 마음대로 정렬하기
# https://velog.io/@dramatic/Algorithm-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0

def solution(strings, n):   

    l=sorted(sorted(strings),key=lambda x:x[n])
    return l