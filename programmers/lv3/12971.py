# https://school.programmers.co.kr/learn/courses/30/lessons/12971
# Summer/Winter Coding(~2018)
# 스티커 모으기(2)

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker)

    dp0 = [0] * len(sticker)
    dp1 = [0] * len(sticker)

    dp0[0] = sticker[0]
    dp0[1] = sticker[0]

    dp1[0] = 0
    dp1[1] = sticker[1]

    for i in range(2, len(sticker) - 1):
        dp0[i] = max(dp0[i - 2] + sticker[i], dp0[i - 1])
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    dp0[-1] = max(dp0[-3], dp0[-2])
    dp1[-1] = max(dp1[-3] + sticker[-1], dp1[-2])

    return max(dp0[-1], dp1[-1])
