# https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 바탕화면 정리

def solution(wallpaper):
    lux = luy = 50
    rdx = rdy = 0
    
    for x, wall in enumerate(wallpaper):
        for y, w in enumerate(wall):
            if w != '#':
                continue
            
            lux = min(lux, x)
            luy = min(luy, y)
            rdx = max(rdx, x + 1)
            rdy = max(rdy, y + 1)

    return [lux, luy, rdx, rdy]
