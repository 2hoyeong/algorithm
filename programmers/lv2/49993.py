# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# Summer/Winter Coding(~2018)
# 스킬트리

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        q = deque(skill)
        for s in skill_tree:
            if s in q:
                n_s = q.popleft()
                if n_s != s:
                    break
        else:
            answer += 1

    return answer
