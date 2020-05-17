# https://programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    height = 3    
    while True:
        width = 3
        yllw = height - 2
        brwn =  width * height - yllw
        while brwn < brown and yllw < yellow:
            width += 1
            brwn += 2
            yllw += (height - 2)
        if brwn == brown and yllw == yellow:
            break
        height += 1
    return [width, height]