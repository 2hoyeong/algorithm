# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환

def getDistance(word, target):
    ret = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            ret += 1
    return ret

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    answer_word = [begin]
    while words:
        for i in answer_word:
            tmp = []
            for word in words:
                if getDistance(i, word) == 1:
                    tmp.append(word)
                    words.remove(word)
        answer += 1
        if target in tmp:
            return answer
        else:
            answer_word = tmp
    
    return answer