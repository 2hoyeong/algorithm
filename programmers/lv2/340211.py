# https://school.programmers.co.kr/learn/courses/30/lessons/340211
# PCCP 기출문제
# 충돌위험 찾기

def solution(points, routes):
    answer = 0
    bots = []
    arrivedPoints = len(routes[0])

    for i in range(len(routes)):
        bots.append([points[routes[i][0] - 1][0], points[routes[i][0] - 1][1], 0])

    while not all(is_arrived(bot, arrivedPoints) for bot in bots):
        for i in range(len(bots)):
            bot = bots[i]
            if is_arrived(bot, arrivedPoints):
                continue
            to = routes[i][bot[2]] - 1
            move(bot, points[to])

        answer += duplicate(bots, arrivedPoints)
        next_point(bots, points, routes)
    return answer

def duplicate(bots, arrivedPoints):
    dups = set()
    filtered_bots = [bot for bot in bots if bot[2] != arrivedPoints]
    for i in range(len(filtered_bots)):
        b1 = filtered_bots[i]
        for j in range(i + 1, len(filtered_bots)):
            b2 = filtered_bots[j]
            if b1[0] == b2[0] and b1[1] == b2[1]:
              dups.add((b1[0], b1[1]))

    return len(dups)

def move(bot, to):
    if bot[0] < to[0]:
        bot[0] += 1
    elif bot[0] > to[0]:
        bot[0] -= 1
    elif bot[1] < to[1]:
        bot[1] += 1
    elif bot[1] > to[1]:
        bot[1] -= 1

def next_point(bots, points, routes):
    for i in range(len(routes)):
        route = routes[i]
        if is_arrived(bots[i], len(route)):
            continue
        to = route[bots[i][2]] - 1
        if bots[i][0] == points[to][0] and bots[i][1] == points[to][1]:
            bots[i][2] += 1

def is_arrived(bot, lastPoint):
    return bot[2] == lastPoint
