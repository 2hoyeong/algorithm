# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십
# 보석 쇼핑

from collections import defaultdict

def solution(gems):
    gems_set = set(gems)
    gems_dict = defaultdict(int)
    start, end = 0, 0
    min_len = 100000
    gems_len = len(gems)

    while end <= gems_len:
        if len(gems_dict) < len(gems_set):
            if end < gems_len:
                gems_dict[gems[end]] += 1
            end += 1
        else:
            while len(gems_dict) == len(gems_set):
                gems_dict[gems[start]] -= 1
                if gems_dict[gems[start]] == 0:
                    del gems_dict[gems[start]]
                start += 1

            if end - start < min_len:
                min_len = end - start
                answer = [start, end]

    return answer
