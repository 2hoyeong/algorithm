# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 햄버거 만들기

def solution(ingredient):
    answer = 0
    st = []
    for ingred in ingredient:
        st.append(ingred)

        while st[-4:] == [1, 2, 3, 1]:
            del st[-4:]
            answer += 1
    return answer
