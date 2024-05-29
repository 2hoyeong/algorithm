# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 키패드 누르기
# 2020 카카오 인턴십

def solution(numbers, hand):
    location = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3,2],
    }
    left = "*"
    right = "#"
    answer = ''
    l_n = [1, 4, 7]
    r_n = [3, 6, 9]

    for n in numbers:
        if n in l_n:
            answer += "L"
            left = n
        elif n in r_n:
            answer += "R"
            right = n
        else:
            l_d = getDistance(location[left], location[n])
            r_d = getDistance(location[right], location[n])
            
            if l_d == r_d:
                if hand == "left":
                    answer += "L"
                    left = n
                else:
                    answer += "R"
                    right = n
            elif l_d > r_d:
                answer += "R"
                right = n
            else:
                answer += "L"
                left = n

    return answer

def getDistance(now, target):
    return abs(now[0] - target[0]) + abs(now[1] - target[1])
