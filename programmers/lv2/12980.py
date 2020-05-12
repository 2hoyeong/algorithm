# https://programmers.co.kr/learn/courses/30/lessons/12980
# 점프와 순간 이동

def solution(n):
    ans = 0
    while n > 0:
        ans += int(n % 2)
        n = n // 2
        
    return ans