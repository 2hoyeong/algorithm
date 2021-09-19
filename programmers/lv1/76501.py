# https://programmers.co.kr/learn/courses/30/lessons/76501
# 월간 코드 챌린지 시즌2
# 음양 더하기

def solution(absolutes, signs):
    return sum([x[0] * (1 if x[1] else -1)  for x in zip(absolutes, signs)])