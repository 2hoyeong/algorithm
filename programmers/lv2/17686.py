# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# [3차] 파일명 정렬
# 2018 KAKAO BLIND RECRUITMENT

import re

class File:
    def __init__(self, name):
        number_str = re.findall("\d+", name)[0]
        head = name.split(number_str)[0]
        self.name = name
        self.head = head.lower()
        self.number_str = number_str
        self.number = int(number_str)

def solution(files):
    answer = []
    for file in files:
        f = File(file)
        
        at = len(answer)
        for i in range(len(answer)):
            if answer[i].head < f.head:
                pass
            elif answer[i].head == f.head:
                if answer[i].number <= f.number:
                    pass
                else:
                    at = i
                    break
            else:
                at = i
                break

        answer.insert(at, f) 
    
    return [x.name for x in answer]
