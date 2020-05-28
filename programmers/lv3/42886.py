# https://programmers.co.kr/learn/courses/30/lessons/42886
# 저울

def solution(weight):
    weight.sort()
    answer = weight[0]
    for w in weight[1:]:
        if answer + 1 >= w:
            answer += w
        else:
            break
    return answer + 1