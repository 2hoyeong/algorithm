# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 숫자 짝꿍

def solution(X, Y):
    xc = {}
    yc = {}
    for x in X:
        if x in xc:
            xc[x] += 1
        else:
            xc[x] = 1
    
    for y in Y:
        if y in yc:
            yc[y] += 1
        else:
            yc[y] = 1

    pair = []
    for k, v in xc.items():
        if k in yc:
            cc = min(v, yc[k])
            pair.extend([k] * cc)

    if not pair:
        return '-1'
    pair.sort(reverse=True)
    if all(p == "0" for p in pair):
        return "0"
    
    return ''.join(pair)
