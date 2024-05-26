# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 택배상자

def solution(order):
    st = []
    answer = 0
    for i in range(1, len(order) + 1):
        if order[answer] == i:
            answer += 1
        else:
            st.append(i)

        while len(st) > 0:
            if st[-1] == order[answer]:
                st.pop()
                answer += 1
            else:
                break
    return answer
