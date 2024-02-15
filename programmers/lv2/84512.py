# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 모음사전

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    w = ''
    
    for a in alphabet:
        w += a
        answer += 1
        if w == word:
            return answer
        for b in alphabet:
            w += b
            answer += 1
            if w == word:
                return answer
            for c in alphabet:
                w += c
                answer += 1
                if w == word:
                    return answer
                for d in alphabet:
                    w += d
                    answer += 1
                    if w == word:
                        return answer
                    for e in alphabet:
                        w += e
                        answer += 1
                        if w == word:
                            return answer
                        w = w[:-1]
                    w = w[:-1]
                w = w[:-1]
            w = w[:-1]
        w = w[:-1]
    return answer
