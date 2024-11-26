# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# PCCP 기출문제
# 동영상 재생기

def to_int(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    
def to_str(time):
    return str(time // 60).zfill(2) + ":" + str(time % 60).zfill(2)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_int(video_len)
    pos = to_int(pos)
    op_start = to_int(op_start)
    op_end = to_int(op_end)

    for command in commands:
        if pos >= op_start and pos <= op_end:
          pos = op_end

        if command == "next":
            pos = pos + 10
            if pos > video_len:
                pos = video_len
        elif command == "prev":
            pos = pos - 10
            if pos < 0:
                pos = 0

    if pos >= op_start and pos <= op_end:
        pos = op_end

    answer = to_str(pos)
    return answer
