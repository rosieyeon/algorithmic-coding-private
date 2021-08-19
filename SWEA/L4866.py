import sys
sys.stdin = open('input.txt')

def chk_brackets (text):
    stack = []
    couple = {')':'(', '}':'{'}
    for brackets in text:
        if brackets in couple.values():
            stack.append(brackets)
        elif brackets in couple.keys():
            if stack: 
                last = stack.pop()
                if couple[brackets] != last:
                        return False
            else: return False
    return True if not stack else False

T = int(input())
for test_case in range(1, T+1):
    text = input()
    print(f'#{test_case}', 1 if chk_brackets(text) else 0)
  