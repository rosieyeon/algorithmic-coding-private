import sys
sys.stdin = open('input.txt')

def calculate_dfs(idx):
    global cnt
    for i in range(len(tree[idx])):
        if tree[idx][i]:
            cnt += 1
            calculate_dfs(tree[idx][i])


for test_case in range(1, int(input())+1):
    E, N = map(int, input().split())
    graph = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]

    for i in range(len(graph)):
        if i%2:
            tree[graph[i]].append(graph[i+1])
    cnt = 1
    calculate_dfs(N)
    print(f'#{test_case} {cnt}')
    