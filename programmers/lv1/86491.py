# https://programmers.co.kr/learn/courses/30/lessons/86491
# 위클리 챌린지
# 최소직사각형

def solution(sizes):
    card_x, card_y = 1, 1
    for x, y in sizes:
        if x > y:
            card_x = max(card_x, x)
            card_y = max(card_y, y)
        else:
            card_x = max(card_x, y)
            card_y = max(card_y, x)
    return card_x * card_y
