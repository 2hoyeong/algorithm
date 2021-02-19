# https://programmers.co.kr/learn/courses/30/lessons/70129
# 월간 코드 챌린지 시즌 1
# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    while s != "1":
        s, zero = convertBinary(s)
        answer[0] += 1
        answer[1] += zero
    return answer

def convertBinary(binary):
    num = "".join([b for b in binary if b != "0"])
    zero = len(binary) - len(num)
    num = bin(len(num))[2:]
    return num, zero