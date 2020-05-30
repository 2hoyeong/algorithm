# https://programmers.co.kr/learn/courses/30/lessons/42588
# 탑

def solution(heights):
    answer = [0] * len(heights)
    while heights:
        top = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > top:
                answer[len(heights)] = i + 1
                break
    return answer