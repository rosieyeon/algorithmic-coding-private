import sys
sys.stdin = open('input.txt')

def dfs(idx, prob):
    global max_val

    if prob <= max_val: return
    if idx == N:
        max_val = prob
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx+1, prob*(arr[idx][i]))
            visited[i] = False


for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
   
    max_val = 0
    visited = [0 for _ in range(N)]

    dfs(0,1)
    print(f'#{test_case} {max_val*100:.6f}')