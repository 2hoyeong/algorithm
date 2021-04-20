# https://programmers.co.kr/learn/courses/30/lessons/76502
# 월간 코드 챌린지 시즌2
# 괄호 회전하기

def solution(s):
    answer = 0
    for i in range(len(s)):
        if isBracket(s):
            answer += 1
        s = s[-1] + s[:-1]
    return answer

def isBracket(s):
    brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    stack = []
    for c in s:
        openBrackets = brackets.values()
        if c in openBrackets:
            stack.append(c)
        else:
            if not stack:
                return False
            elif brackets[c] == stack[-1]:
                stack.pop()
    return stack == []