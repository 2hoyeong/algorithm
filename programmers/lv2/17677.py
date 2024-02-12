# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 2018 KAKAO BLIND RECRUITMENT
# 뉴스 클러스터링

import re

def solution(str1, str2):
    rg = re.compile('^[a-z]+$')
    str1 = str1.lower()
    str2 = str2.lower()
    str1_array = []
    str2_array = []
    for i in range(len(str1) - 1):
        str1_array.append(str1[i:i+2])

    for i in range(len(str2) - 1):
        str2_array.append(str2[i:i+2])
    
    str1_array = list(filter(lambda x: rg.match(x), str1_array))
    str2_array = list(filter(lambda x: rg.match(x), str2_array))
    
    A = []
    str2_array_c = str2_array.copy()
    for s in str1_array:
        if s in str2_array_c:
            A.append(s)
            str2_array_c.remove(s)
    
    B = str2_array.copy()
    a_copy = A.copy()
    for s in str1_array:
        if s not in a_copy:
            B.append(s)
        else:
            a_copy.remove(s)

    if len(B) == 0:
        return 65536
    
    return int(len(A) / len(B) * 65536)
