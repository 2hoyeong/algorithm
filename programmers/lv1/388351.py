# https://school.programmers.co.kr/learn/courses/30/lessons/388351
# 2025 프로그래머스 코드챌린지 1차 예선
# 유연근무제

def solution(schedules, timelogs, startday):
    answer = len(schedules)
    if startday < 7:
        saturday = 6 - startday
    else:
        saturday = 6
    sunday = 7 - startday
    
    for i, schedule in enumerate(schedules):
        schedule_hour = schedule // 100
        schedule_minute = schedule - schedule_hour * 100
        schedule_time = schedule_hour * 60 + schedule_minute

        for j, timelog in enumerate(timelogs[i]):
            if j == saturday or j == sunday:
                continue
            hour = timelog // 100
            minute = timelog - hour * 100
            time = hour * 60 + minute
            if time - schedule_time > 10:
                answer -= 1
                break
    
    return answer
