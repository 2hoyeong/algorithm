# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭
# https://velog.io/@dramatic/Algorithm-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD

def solution(bridge_length, weight, truck_weights):
    i = 0
    j = 0
    onweight = 0
    time = [0] * len(truck_weights)
    while i < len(truck_weights):
        if truck_weights[i] + onweight <= weight:
            onweight += truck_weights[i]
            i += 1
        for k in range(i):
            time[k] += 1
        if time[j] >= bridge_length:
            onweight -= truck_weights[j]
            j += 1
    
    return time[0] + bridge_length