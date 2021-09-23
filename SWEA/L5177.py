import sys
import pdb
sys.stdin = open('input.txt')

def mk_heap(x):
    tree.append(x)
    node = tree.index(x)
    if len(tree) > 2:
        while tree[node] < tree[node//2]: 
            tree[node], tree[node//2] = tree[node//2], tree[node]
            node = node//2

def sum_parents_node(x):
    node = tree.index(x)
    cnt = 0
    while node > 1:
        # pdb.set_trace()
        cnt += tree[node//2]
        node = node//2
    return cnt

for test_case in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0]

    for i in range(N):
        mk_heap(numbers[i])
    
    print(f'#{test_case} {sum_parents_node(tree[-1])}')