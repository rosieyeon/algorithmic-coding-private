import sys
sys.stdin = open('input.txt')

T = int(input())

# 지정된 크기만큼 파리를 죽여봅시다.
def kill_flies(y, x):
    cnt = 0
    for i in range(y, y+M):
        for j in range(x, x+M):
            cnt += flies[i][j]
    return cnt
    
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    # 죽인 파리의 크기를 비교해 봅시다
    for y in range(N-M+1):
        for x in range(N-M+1):
            if max_flies < kill_flies(y,x):
                max_flies = kill_flies(y,x)
            
    print(f'#{test_case} {max_flies}')