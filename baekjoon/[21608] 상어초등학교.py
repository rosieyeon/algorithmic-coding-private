# import pdb
# from pprint import pprint
# import sys
# sys.stdin = open('input.txt')

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

N = int(input())
preferred = [[] for _ in range(N**2+1)]
arr = [[0]*N for _ in range(N)]
cnt = 0

for _ in range(N**2):
    tmp = list(map(int, input().split()))
    preferred[tmp[0]] = tmp[1:]

    # 이 부분을 0으로 초기화했다가 계속 에러났음
    # 좋아하는 친구도, 빈 자리도 주변에 하나도 없을 경우를 생각해주어야한다!
    max_likecnt = -1
    max_emptycnt = -1
    
    for x in range(N):
        for y in range(N):
            if not arr[x][y]:
                likecnt = 0
                emptycnt = 0
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<N and 0<=ny<N:
                        if arr[nx][ny] in preferred[tmp[0]]:
                            likecnt += 1
                        if not arr[nx][ny]:
                            emptycnt += 1
                if max_likecnt < likecnt or (max_likecnt==likecnt and max_emptycnt<emptycnt):
                    max_likecnt = likecnt
                    max_emptycnt = emptycnt
                    tmp_seat = [x,y]
                    
    arr[tmp_seat[0]][tmp_seat[1]] = tmp[0]

cnt = 0
for r in range(N):
    for c in range(N):
        like = 0
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N:
                if (arr[nr][nc] in preferred[arr[r][c]]):
                    like += 1
        if like:
            cnt += 10**(like-1)
print(cnt)

