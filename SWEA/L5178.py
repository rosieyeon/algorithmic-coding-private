import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    leaf_node = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N+2)
    for i in range(M):
        tree[leaf_node[i][0]] = leaf_node[i][1]
    
    for i in range(N-M, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1] 
    
    print(f'#{test_case} {tree[L]}')