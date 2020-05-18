# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        maxhuman = sum([mid // x for x in times])
        
        if maxhuman >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer