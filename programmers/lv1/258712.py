# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2024 KAKAO WINTER INTERNSHIP
# 가장 많이 받은 선물

from itertools import permutations

def solution(friends, gifts):
    friends_permut = permutations(friends, 2)
    friends_info = { friend : 0 for friend in friends }
    friends_gift = { friend : 0 for friend in friends }
    friends_dict = { fromm + "_" + to : 0 for fromm, to in friends_permut }
    for gift in gifts:
        fromm, to = gift.split(" ")
        key = fromm + "_" + to
        friends_dict[key] = friends_dict[key] + 1
    
    for k, v in friends_dict.items():
        if v == -1:
            continue

        f, t = k.split("_")
        friends_info[f] += v
        friends_info[t] -= v
    
        rk = t + "_" + f
        rv = friends_dict[rk]
        friends_info[t] += rv
        friends_info[f] -= rv
        
        if v == rv:
            continue
        
        if v > rv:
            friends_gift[f] += 1
        elif v < rv:
            friends_gift[t] += 1
        
        friends_dict[k] = -1
        friends_dict[rk] = -1
    

    for k, v in friends_dict.items():
        if v == -1:
            continue
        
        f, t = k.split("_")
        if friends_info[f] > friends_info[t]:
            friends_gift[f] += 1
        elif friends_info[f] < friends_info[t]:
            friends_gift[t] += 1
        
        rk = t + "_" + f
        friends_dict[rk] = -1
        friends_dict[k] = -1
        
        
    answer = max(friends_gift.values())
    return answer
