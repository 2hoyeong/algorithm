# https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 월간 코드 챌린지 시즌1
# 쿼드압축 후 개수 세기

def solution(arr):
  answer = [0, 0]
  def dfs(x, y, n):
    nonlocal answer
    for i in range(x, x+n):
      for j in range(y, y+n):
        if arr[x][y] != arr[i][j]:
          dfs(x, y, n//2)
          dfs(x+n//2, y, n//2)
          dfs(x, y+n//2, n//2)
          dfs(x+n//2, y+n//2, n//2)
          return

    answer[arr[x][y]] += 1

  dfs(0, 0, len(arr))
  return answer
