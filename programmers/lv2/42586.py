# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

def solution(progresses, speeds):
    answer = []
    func = 0
    
    while progresses:
        progresses = [x + speeds[i] for i, x in enumerate(progresses)]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            func += 1
            
        if func:
            answer.append(func)
            func = 0
    return answer
