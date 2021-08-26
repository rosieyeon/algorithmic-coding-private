import sys
sys.stdin = open('input.txt')

def find_route(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny]:
            if not maze[nx][ny]:
                visited[nx][ny] = 1
                find_route(nx, ny)
            elif maze[nx][ny] == 3:
                visited[nx][ny] = 3
                return True
    return True if visited[goal_x][goal_y] else False

for test_case in range(1, 11):
    input()
    maze = [list(map(int,input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 3: goal_x, goal_y = i, j
            elif maze[i][j] == 2: start_x, start_y = i, j
   
    print(f'#{test_case}', 1 if find_route(start_x, start_y) else 0)

