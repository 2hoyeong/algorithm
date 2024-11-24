# https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 2019 카카오 개발자 겨울 인턴십
# 불량 사용자

import itertools

def solution(user_id, banned_id):
    o = {}
    for b, banned in enumerate(banned_id):
        for user in user_id:
            if len(user) != len(banned):
                continue
            for i in range(len(banned)):
                if banned[i] == "*":
                    continue
                if user[i] != banned[i]:
                    break
            else:
                if b in o:
                    o[b].add(user)
                else:
                    o[b] = set([user])

    data = (list(o[key]) for key in sorted(o.keys()) if o[key])
    combinations = list(itertools.product(*data))


    duplicates = set()
    for combination in combinations:
        if len(set(combination)) == len(combination):
            duplicates.add(tuple(sorted(combination)))
        
    return len(duplicates)
