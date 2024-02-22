# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 월간 코드 챌린지 시즌2
# 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
            continue

        bsn = list(str(bin(n)).replace('0b', ''))
        if n + 1 & n == 0:
            bn = ['1'] + bsn
            bn[1] = '0'
            answer.append(int(''.join(bn), 2))
            continue
        
        
        for j in range(len(bsn) - 1, -1, -1):
            if bsn[j] != '1':
                bsn[j] = '1'
                bsn[j + 1] = '0'
                answer.append(int(''.join(bsn), 2))
                break

    return answer
