# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환
# 2020 KAKAO BLIND RECRUITMENT

def isBalancedBasket(s):
    return len(s) > 0 and s.count("(") == s.count(")")

def isCorrectBasket(s):
    if not isBalancedBasket(s):
        return False
    tmp = []
    for c in s:
        if tmp:
            if tmp[-1] + c == "()":
                tmp.pop()
            else:
                tmp.append(c)
        else:
            tmp.append(c)
            
    return len(tmp) == 0

def reverseBasket(s):
    tmp = []
    for c in s:
        if c == "(":
            tmp.append(")")
        elif c == ")":
            tmp.append("(")
    return ''.join(tmp)

def makeBasket(s):
    if isCorrectBasket(s) or s == "":
        return s
    u = []
    i = 0
    while not isBalancedBasket(u):
        u = s[:i]
        i += 1
    v = s[i - 1:]
    if isCorrectBasket(u):
        return u + makeBasket(v)
    
    return "(" + makeBasket(v) + ")" + reverseBasket(u[1:-1])

def solution(p):
    return makeBasket(p)