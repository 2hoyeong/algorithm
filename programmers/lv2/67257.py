# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴쉽
# 수식 최대화

import itertools
import re

def solution(expression):
    op = ['*', '+', '-']
    priors = list(itertools.permutations(op))
    token = re.findall(re.compile('(\d+|[^ 0-9])'), expression)
    answer = 0
    for prior in priors:
        answer = max(answer, abs(postfix(token, list(prior))))
        
    return answer

def postfix(exp, op):
    post = []
    stk = []
    for e in exp:
        if e in op:
            prior = op.index(e)
            while len(stk) > 0:
                if prior < op.index(stk[-1]):
                    break
                post.append(stk.pop())
            stk.append(e)
        else:
            post.append(e)
    while len(stk) > 0:
        post.append(stk.pop())
        
    return calc(post)

def calc(postfix):
    stk = []
    op = ['*', '+', '-']
    for exp in postfix:
        if exp in op:
            op2 = stk.pop()
            op1 = stk.pop()
            stk.append(str(eval(op1 + exp + op2)))
        else:
            stk.append(exp)
    return int(stk[0])