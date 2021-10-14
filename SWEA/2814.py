import sys
sys.stdin = open('input.txt')

def dfs(n, distance):
    global answer
    answer = max(answer, distance)
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i, distance+1)
            visited[i] = False

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * (N+1)
    answer = 0

    for i in range(1, N+1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    
    print(f'#{test_case} {answer}')
