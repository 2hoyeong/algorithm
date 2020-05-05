# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수

def solution(x):
    e = sum([int(e) for e in str(x)])
    return x % e == 0
	