# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 2022 KAKAO BLIND RECRUITMENT
# 주차 요금 계산

import math

def solution(fees, records):
    base_m, base_p, m, p = fees
    parking = {}
    use_time = {}
    for record in records:
        time, car, op = record.split(" ")
        if op == "IN":
            parking[car] = time
        else:
            in_time = hToM(parking[car])
            out_time = hToM(time)
            gap = out_time - in_time
            if car in use_time:
                use_time[car] += gap
            else:
                use_time[car] = gap
            del parking[car]

    for no_out_car in parking:
        in_time = hToM(parking[no_out_car])
        out_time = hToM('23:59')
        gap = out_time - in_time

        if no_out_car in use_time:
            use_time[no_out_car] += gap
        else:
            use_time[no_out_car] = gap

    car_numbers = sorted(list(use_time.keys()))
    answer = []
    for num in car_numbers:
        time = use_time[num]
        price = base_p + (math.ceil(max(time - base_m, 0) / m) * p)
        answer.append(price)
    
    return answer

def hToM(hs):
    h, m = hs.split(":")
    return int(m) + (int(h) * 60)
