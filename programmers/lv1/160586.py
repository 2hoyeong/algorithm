# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 대충 만든 자판

def solution(keymaps, targets):
    km = {}
    for keymap in keymaps:
        for i, key in enumerate(keymap):
            if key in km:
                km[key] = min(km[key], i + 1)
            else:
                km[key] = i + 1

    answer = []
    for target in targets:
        index = 0
        for c in target:
            if c in km:
                index += km[c]
            else:
                index = -1
                break
        answer.append(index)
    return answer
