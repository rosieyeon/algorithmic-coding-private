import sys
sys.stdin = open('input.txt')

def calculate (exp):
    stack = []
    for char in exp:
        if char.isdigit(): stack.append(char)
        else:
            if char == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif char == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif char == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) - int(right))
            elif char == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) / int(right))
    return stack[0]


def make_postfix_exp (formula):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 3}

    result = ''
    stack = []

    for char in formula:
        if char.isdigit(): result += char
        else:
            while stack and isp[stack[-1]] > icp[char]:
                result += stack.pop()
            stack.append(char)
    while stack : result += stack.pop()

    return result

for test_case in range(1, 11):
    input()
    formula = input()
    postfix_exp = make_postfix_exp(formula)

    print(f'#{test_case} {calculate(postfix_exp)}')

