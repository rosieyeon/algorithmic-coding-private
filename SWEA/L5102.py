import sys
sys.stdin = open('input.txt')

from collections import deque

def find_route_bfs(graph, visited, start, end):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        node = q.popleft()
        for x in graph[node]:
            if not visited[x]:
                visited[x] = visited[node] + 1
                q.append(x)
    return True if visited[end] else False 


for test_case in range(1, int(input())+1):
    V, E = map(int,input().split())
    nodes = [[] for _ in range(V+1)]

    for i in range(E):
        num1, num2 = map(int, input().split())
        nodes[num1].append(num2)
        nodes[num2].append(num1)
   
    S, G = map(int, input().split())
    stack = [0 for _ in range(V+1)] # 방문한 노드를 True로 바꿔줄 예정

    print(f'#{test_case}', stack[G]-1 if find_route_bfs(nodes, stack, S, G) else 0)
     