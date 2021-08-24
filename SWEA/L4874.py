import sys
sys.stdin = open('input.txt')

def calculate (exp):
    stack = []
    try:
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
                    stack.append(int(left) // int(right))
                elif char == '.':
                    return stack[0]
    except:
        return False


for test_case in range(1, int(input())+1):
    formula = list(input().split())
    print(f'#{test_case}', calculate(formula) if type(calculate(formula)) == int else 'error')
