import sys
sys.stdin = open('input.txt')

def find_route(graph, visited, start, end):
    visited[start] = True
    adj_list = graph[start]
    for adj in adj_list:
        if not visited[adj]:
            find_route(graph, visited, adj, end)
    return True if visited[end] else False  

for _ in range(10):
    test_case, n = map(int, input().split())
    nodes = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(0, len(nodes), 2):
        graph[nodes[i]].append(nodes[i+1])

    stack = [0 for _ in range(100)] # 방문한 노드를 True로 바꿔줄 예정
    
    print(f'#{test_case}', 1 if find_route(graph, stack, 0, 99) else 0)

