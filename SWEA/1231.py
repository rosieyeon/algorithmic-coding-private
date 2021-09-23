import sys
sys.stdin = open('input.txt')

def in_order(x):
    if x > N:
        return ''
    else:
        return in_order(2*x) + tree[x] + in_order(2*x+1)

for test_case in range(1, 11):
    N = int(input())
    tree = [0]

    for _ in range(N):
        info = input().split()
        char = info[1]
        # 완전 이진트리니까 그냥 append
        tree.append(char)
    
    print(f'#{test_case}', in_order(1))