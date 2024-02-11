# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 둘만의 암호

def solution(s, skip, index):
    a = 97
    alphabet = [chr(a + i) for i in range(26)]
    filtered = list(filter(lambda x: x not in skip, alphabet))

    answer = ''
    for c in s:
        answer += filtered[(filtered.index(c) + index) % len(filtered)]
    return answer