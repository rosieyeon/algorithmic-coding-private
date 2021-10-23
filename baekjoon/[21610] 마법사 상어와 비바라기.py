import pdb
from pprint import pprint

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

DIRECTIONS = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
DIAGONAL = [(-1,-1), (-1,1), (1,1), (1,-1)]
clouds = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]


def vap(arr, x, y):
    cnt = 0
    for dx, dy in DIAGONAL:
        if 0 <= x+dx < N and 0 <= y+dy < N and arr[x+dx][y+dy]:
            cnt += 1
    return cnt

for i in range(M):
    visited = [[0]*N for _ in range(N)]
    di = move[i][0]
    si = move[i][1]
    for cloud in clouds:
        cloud[0] = (cloud[0] + DIRECTIONS[di-1][0]*si) %N
        cloud[1] = (cloud[1] + DIRECTIONS[di-1][1]*si) %N
        arr[cloud[0]][cloud[1]] += 1  # 비가 옴
        visited[cloud[0]][cloud[1]] = 1
    
    for cloud in clouds:  # 대각선에 있는 물의 존재만큼 증가
        arr[cloud[0]][cloud[1]] += vap(arr, cloud[0], cloud[1])

    new_clouds = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2 and not visited[r][c]: 
                new_clouds.append([r,c])
                arr[r][c] -= 2
    clouds = new_clouds

res = 0
for x in arr:
    res += sum(x)
print(res)
