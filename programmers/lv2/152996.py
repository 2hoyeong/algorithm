# https://school.programmers.co.kr/learn/courses/30/lessons/152996
# 시소 짝꿍

from collections import defaultdict, Counter

def solution(weights):
    weights.sort()
    weights_compare = defaultdict(int)
    weights_counter = Counter(weights)
    answer = 0

    for i in range(len(weights)):
        weight = weights[i]
        answer += weights_compare.get(weight * 2, 0) + weights_compare.get(weight * 3, 0) + weights_compare.get(weight * 4, 0)

        if weights_counter[weight] > 1:
            answer -= (weights_counter[weight] - 1)

        weights_compare[weight * 4] += 1
        weights_compare[weight * 3] += 1
        weights_compare[weight * 2] += 1

    return answer
