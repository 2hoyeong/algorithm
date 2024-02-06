# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 월간 코드 챌린지 시즌3
# n^2 배열 자르기

def solution(n, left, right):
    answer = []
    lefti = left // n
    leftj = left % n
    
    righti = right // n
    rightj = right % n
    for i in range(lefti, righti + 1):
        for _ in range(i):
            answer.append(i + 1)
        for j in range(i, n):
            answer.append(j + 1)

    rightslice = n - (rightj + 1 )
    if rightslice == 0:
        return answer[leftj:]

    return answer[leftj:-rightslice]
