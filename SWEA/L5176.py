import sys
sys.stdin = open('input.txt')

def in_order(x):
    if x <= N:
        in_order(2*x)
        res.append(tree[x])
        in_order(2*x+1)
        

for test_case in range(1, int(input())+1):
    N = int(input())
    tree = list(range(N+1))
    res = [0]

    in_order(1)
    print(f'#{test_case} {res.index(1)} {res.index(N//2)}')
