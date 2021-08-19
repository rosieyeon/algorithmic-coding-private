import sys
sys.stdin = open('input.txt')

# dfs를 이용해서 경로 구하기
def find_route(graph, visited, start, end):
    visited[start] = True
    adj_list = graph[start]
    for adj in adj_list:
        if not visited[adj]:
            find_route(graph, visited, adj, end)
    return True if visited[end] else False  


for test_case in range(1, int(input())+1):
    V, E = map(int,input().split())
    nodes = [[] for _ in range(V+1)]

    for i in range(E):
        num1, num2 = map(int, input().split())
        nodes[num1].append(num2)
   
    S, G = map(int, input().split())
    stack = [0 for _ in range(V+1)] # 방문한 노드를 True로 바꿔줄 예정
    
    print(f'#{test_case}', 1 if find_route(nodes, stack, S, G) else 0)
