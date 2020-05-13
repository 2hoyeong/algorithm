# https://programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑

answer = []

def hanoi(n, f, t, a):
    if n == 1:
        answer.append([f, t])
        return
    hanoi(n - 1, f, a, t)
    answer.append([f, t])
    hanoi(n - 1, a, t, f)

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer