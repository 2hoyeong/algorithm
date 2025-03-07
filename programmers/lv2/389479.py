# https://school.programmers.co.kr/learn/courses/30/lessons/389479
# 2025 프로그래머스 코드 챌린지 2차 예선
# 서버 증설 횟수

def solution(players, m, k):
    servers = [25]
    answer = 0
    next_server = 0
    for i in range(24):
        n = players[i]
        servers = list(filter(lambda x: x + k > i, servers))
        
        while len(servers) * m <= n:
            servers.append(i)
            answer += 1

    return answer
