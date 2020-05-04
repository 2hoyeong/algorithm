# https://programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이
# Summer/Winter Coding(~2018)
# https://velog.io/@dramatic/Algorithm-%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4

def solution(dirs):
    answer = 0
    roads = set()
    position = (5, 5)
    next_position = (0, 0)
    dirs = list(dirs)
    for w in dirs:
        if w == "U":
            next_position = (position[0], max(0, position[1] - 1))
        elif w == "D":
            next_position = (position[0], min(10, position[1] + 1))
        elif w == "R":
            next_position = (min(10, position[0] + 1), position[1])
        elif w == "L":
            next_position = (max(0, position[0] - 1), position[1])
            
        if next_position != position and (next_position, position) not in roads:
            roads.add((position, next_position))
            roads.add((next_position, position))
            answer +=1
        position = next_position
        
    return answer