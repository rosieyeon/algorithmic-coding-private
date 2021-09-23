import sys
sys.stdin = open('input.txt')

def calculate(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


for test_case in range(1, 11):
    N = int(input())
    tree = [[0]] + [list(input().split()) for _ in range(N)]

    for i in range(N, 0, -1):
        node = tree[i]
        if len(node) == 4:
            left = tree[int(node[2])][1]
            right = tree[int(node[3])][1]
            operator = node[1]
            tree[i] = [i, calculate(int(left), int(right), operator)]
    
    print(f'#{test_case} {int(tree[1][1])}')
