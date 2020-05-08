# https://programmers.co.kr/learn/courses/30/lessons/17684
# 압축
# 2018 KAKAO BLIND RECRUITMENT

def solution(msg):
    answer = []
    dic = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    words = msg[0]
    i = 1
    while i < len(msg):
        if words + msg[i] not in dic:
            answer.append(dic.index(words) + 1)
            dic.append(words + msg[i])
            words = msg[i]
        else:
            words += msg[i]
        i += 1
    answer.append(dic.index(words) + 1)
    return answer