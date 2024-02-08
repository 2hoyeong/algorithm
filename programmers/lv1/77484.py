# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    zeros = 0
    wins = 0
    for n in lottos:
        if n == 0:
            zeros += 1
        if n in win_nums:
            wins += 1
            
    return [min(7 - wins - zeros, 6), min(7 - wins, 6)]
