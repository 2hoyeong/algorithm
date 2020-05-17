# https://programmers.co.kr/learn/courses/30/lessons/42897
# 도둑질

def solution(money):
    answer = 0
	
	# 첫 집을 털 경우
    steal = [0] * len(money)
    steal[0] = money[0]
    steal[1] = money[0]
    for i in range(2, len(money)):
        steal[i] = max(steal[i - 1], money[i] + steal[i - 2])
    answer = steal[-2]

	# 첫 집을 안 털 경우
    steal[0] = 0
    steal[1] = money[1]
    for i in range(2, len(money)):
        steal[i] = max(steal[i - 1], money[i] + steal[i - 2])
    answer = max(answer, steal[-1])
    
    return answer