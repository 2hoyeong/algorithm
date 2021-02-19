# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 KAKAO BLIND RECRUITMENT
# 오픈채팅방

def solution(record):
    answer = []
    name = {}
    action = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for r in record:
        r = r.split(" ")
        if r[0] == "Leave":
            continue
        uid = r[1]
        name[uid] = r[2]
        
    for r in record:
        r = r.split(" ")
        if r[0] == "Change":
            continue
        answer.append(name[r[1]] + action[r[0]])
    return answer