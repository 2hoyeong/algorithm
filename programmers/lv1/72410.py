# https://programmers.co.kr/learn/courses/30/lessons/72410
# 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천

import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^\w\-.]', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = answer[1:] if answer[0] == '.' else answer
    answer = answer[:-1] if answer[-1:] == '.' else answer
    answer = answer == '' and 'a' or answer
    answer = answer[:15]
    answer = answer[:-1] if answer[-1:] == '.' else answer
    answer = answer + answer[-1] * (3 - len(answer)) if len(answer) <= 2 else answer
    return answer