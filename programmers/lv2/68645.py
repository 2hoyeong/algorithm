# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 월간 코드 챌린지 시즌1
# 삼각 달팽이

def solution(n):
    last = n * (n + 1) // 2
    answer = [0] * last
    x, y = -1, 0
    num = 1
    for i in range(n):
      for _ in range(i, n):
        if i % 3 == 0:
          x += 1
        elif i % 3 == 1:
          y += 1
        else:
          x -= 1
          y -= 1
        answer[x * (x + 1) // 2 + y] = num
        num += 1
            
    return answer
