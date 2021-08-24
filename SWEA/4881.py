import sys
sys.stdin = open('input.txt')

def find_minimum (idx, tmp_sum): 
    global glob_min
    if idx == N :
        if tmp_sum < glob_min:
            glob_min = tmp_sum
        return 

    if tmp_sum > glob_min:
        return 
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find_minimum(idx+1, tmp_sum + arr[idx][i])
            visited[i] = False
    
    
for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    glob_min = 10*10
    visited = [0 for _ in range(N)]
    find_minimum(0,0)

    print(f'#{test_case} {glob_min}')