# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT
# https://velog.io/@dramatic/Algorithm-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95

def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        a = 0
        tmp = []
        stmp = s
        while stmp:
            sliced = stmp[:i]
            stmp = stmp[i:]
            if tmp:
                if tmp[-1][1] == sliced:
                    tmp[-1][0] += 1
                else:
                    tmp.append([1, sliced])
            else:
                tmp.append([1, sliced])
        for t in tmp:
            a += len(t[1]) + (t[0] > 1) * len(str(t[0]))
        answer = min(answer, a)
    return answer
	