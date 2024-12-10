# https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 호텔 대실

def solution(book_time):
    for i in range(len(book_time)):
        bt = book_time[i]
        start_h, start_m = map(int, bt[0].split(":"))
        start_time = start_h * 60 + start_m
        end_h, end_m = map(int, bt[1].split(":"))
        end_time = end_h * 60 + end_m + 10
        book_time[i] = [start_time, end_time]
    
    book_time.sort(key=lambda x: x[0])
    queue = [book_time[0][1]]
    max_queue = 1
    for i in range(1, len(book_time)):
        start_time, _ = book_time[i]
        j = 0
        while j < len(queue):
            if queue[j] <= start_time:
                queue.pop(j)
            else:
                j += 1
        queue.append(book_time[i][1])
        max_queue = max(max_queue, len(queue))

    return max_queue
