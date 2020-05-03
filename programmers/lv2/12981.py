# https://programmers.co.kr/learn/courses/30/lessons/12981
# Summer/Winter Coding(~2018)
# 영어 끝말잇기

def solution(n, words):
    prev_words = set([words[0]])
    prev_word = words[0]

    for i in range(1, len(words)):
        if prev_word[-1] != words[i][0] or words[i] in prev_words:
            return [(i % n) + 1, int(i / n) + 1]
        prev_word = words[i]
        prev_words.add(words[i])
        
    return [0, 0]