# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기
# 2022 KAKAO TECH INTERNSHIP

def solution(survey, choices):
    score = { "RT": 0, "CF": 0, "JM": 0, "AN": 0 }
    needChanged = { "T": True, "F": True, "M": True, "N": True, "R": False, "C": False, "J": False, "A": False }
    for s, c in zip(survey, choices):
        changed = needChanged[s[0]]
        s = ''.join(sorted(s))
        if changed:
            score[s] += 4 - c
        else:
            score[s] += c - 4

    answer = ''
    for k in score.keys():
        if score[k] <= 0:
            answer += k[0]
        else:
            answer += k[1]
    
    return answer
