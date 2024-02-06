# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# PCCP 기출문제
# 붕대 감기

def solution(bandage, health, attacks):
    answer = health
    lastAttack = [0, 0]
    cast, heal, addHeal = bandage
    for [time, damage] in attacks:
        gapTime = time - lastAttack[0] - 1
        answer = min(health, answer + gapTime * heal)
        answer = min(health, answer + gapTime // cast * addHeal)
        answer -= damage
        if answer < 1:
            return -1
        lastAttack = [time, damage]
    
    return answer
