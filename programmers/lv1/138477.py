# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 명예의 전당 (1)

from queue import PriorityQueue

def solution(k, score):
    answer = []
    que = PriorityQueue(maxsize=k)
    que.put(score[0])
    for s in score[1:]:
        minimum = que.get()
        que.put(max(s, minimum))
        answer.append(minimum)
        if not que.full():
            que.put(min(s, minimum))
    answer.append(que.get())
    return answer
