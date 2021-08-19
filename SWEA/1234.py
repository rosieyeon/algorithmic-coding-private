import sys
sys.stdin = open('input.txt')

for test_case in range(1, 10+1):
    n, text = input().split()
    stack = []

    for char in text:
        if stack:
            # stack에 뭐라도 하나 있는 상황에서
            # stack에 있는 마지막 문자가 내가 넣은 문자랑 똑같으면 없애버림
            if stack[-1] == char:
                stack.pop()
            # 안똑같으면 그냥 얌전히 추가해줌
            else: stack.append(char)
        else: stack.append(char)

    print(f'#{test_case} ', *stack, sep='')