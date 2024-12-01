# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 2022 KAKAO TECH INTERNSHIP
# 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    q1_sum = sum(queue1)
    queue2 = deque(queue2)
    q2_sum = sum(queue2)

    mid = (sum(queue1) + sum(queue2)) // 2

    for _ in range(3 * len(queue1)):
        if q1_sum == q2_sum:
            return answer
        
        if q1_sum < mid:
            q2_pop = queue2.popleft()
            q1_sum += q2_pop
            q2_sum -= q2_pop
            queue1.append(q2_pop)
        else:
            q1_pop = queue1.popleft()
            q1_sum -= q1_pop
            q2_sum += q1_pop
            queue2.append(q1_pop)

        answer += 1

    return -1
