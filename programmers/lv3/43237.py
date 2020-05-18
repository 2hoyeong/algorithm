# https://programmers.co.kr/learn/courses/30/lessons/43237
# 예산

def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)
    answer = 0
    left = 0
    right = max(budgets)
    while left <= right:
        mid = (right + left) // 2
        limit_M = sum([min(x, mid) for x in budgets])
        if limit_M > M:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer