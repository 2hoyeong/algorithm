# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자
# https://velog.io/@dramatic/Algorithm-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90

def solution(n):
    numbers = ['4', '1', '2']
    answer = ''
    while n != 0:
        answer = numbers[n % 3] + answer
        n = n // 3
    return answer
	