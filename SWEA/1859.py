import sys
import pdb
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))

    stack = []
    result = 0

    for i in range(len(price)-1, -1, -1):
        if stack:
            if price[i] < stack[-1]:
                result += stack[-1] - price[i]
            else:
                stack.append(price[i])
        else:
            stack.append(price[i]) 
    print(f'#{test_case} {result}')
