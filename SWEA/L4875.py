import sys
from pprint import pprint
sys.stdin = open('input.txt')

def find_route(visited, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if not maze[nx][ny]:
                visited[nx][ny] = True
                if find_route(visited, nx, ny):
                    return True
                find_route(visited, nx, ny)
            elif maze[nx][ny] == 3:
                return True
    

for test_case in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    if find_route(visited, start_x, start_y) == True:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)

    # print(f'#{test_case}', 1 if find_route(visited, start_x, start_y) else 0)
