# https://programmers.co.kr/learn/courses/30/lessons/82612
# 위클리 챌린지
# Summer/Winter Coding(~2018)

def solution(price, money, count):
    answer = -1
    weight = ((count + 1) * count) / 2
    total = price * weight
    if total > money:
        return total - money
    return 0