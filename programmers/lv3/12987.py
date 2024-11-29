# https://school.programmers.co.kr/learn/courses/30/lessons/12987
# Summer/Winter Coding(~2018)
# 숫자 게임

def solution(A, B):
  answer = 0

  A.sort(reverse=True)
  B.sort(reverse=True)

  j = 0
  for i in range(len(A)):
    if A[i] < B[j]:
      j += 1
      answer += 1

  return answer
