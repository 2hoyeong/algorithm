# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

def solution(s):
    q = [s[0]]
    if s.count("(") != s.count(")"):
        return False
    
    for c in s[1:]:
        if c == "(":
            q.append(c)
        elif c == ")":
            if q:
                q.pop()
    return q == []