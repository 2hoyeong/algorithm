# https://school.programmers.co.kr/learn/courses/30/lessons/340210
# PCCP 기출문제
# 수식 복원하기

def to_base(n, base):
    result = ""
    while n > 0:
        result = str(n % base) + result
        n = n // base
    return result

class Expression:
    def __init__(self, expression):
        [self.num1, self.op, self.num2, _, self.result] = expression.split(" ")
        self.base = [2, 9]
        self.target = bool(self.result == "X")

        self.base[0] = max(max([int(digit) for digit in self.num1]) + 1, self.base[0])
        self.base[0] = max(max([int(digit) for digit in self.num2]) + 1, self.base[0])
        if not self.is_target():
            self.base[0] = max(max([int(digit) for digit in self.result]) + 1, self.base[0])
        
        self.x = False
        
    def __str__(self):
        if self.x or self.result == "X":
            return f"{self.num1} {self.op} {self.num2} = ?"
        
        return f"{self.num1} {self.op} {self.num2} = {self.result if self.result else '0'}"

    def is_target(self):
        return self.target
    
    def infer_base(self):
        bases = []
        for base in range(self.base[0], self.base[1] + 1):
            if self.calculate(base) == str(self.result):
                bases.append(base)
        if bases:
            self.base = [min(bases), max(bases)]

    def calculate(self, base):
        if self.op == "+":
            return to_base((int(self.num1, base) + int(self.num2, base)), base)
        elif self.op == "-":
            return to_base((int(self.num1, base) - int(self.num2, base)), base)
        
    def done(self):
        return self.base[0] == self.base[1]

def solution(expressions):
    expression_classes = []
    for expression in expressions:
        expression_classes.append(Expression(expression))
  
    base = [2, 9]
    for expression in expression_classes:
        if not expression.is_target():
            expression.infer_base()
        base[0] = max(base[0], expression.base[0])
        base[1] = min(base[1], expression.base[1])

        if expression.done():
            break

    for expression in expression_classes:
        if expression.is_target():
            for b in range(base[0], base[1] + 1):
                if not expression.x:
                    if expression.calculate(b) != expression.result and expression.result != "X":
                        expression.x = True

                    expression.result = expression.calculate(b)

    answer = []
    for expression in expression_classes:
        if expression.is_target():
            answer.append(str(expression))
    return answer
