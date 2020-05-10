# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

def solution(priorities, location):
    answer = 0
    while True:
        max_p = max(priorities)
        if priorities[0] < max_p:
            priorities.append(priorities.pop(0))
        else:
            answer += 1
            if location == 0:
                break
            priorities.pop(0)
        location = (location - 1) % len(priorities)    
    return answer
	