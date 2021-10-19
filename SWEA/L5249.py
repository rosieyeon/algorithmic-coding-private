import sys
sys.stdin = open('input.txt')

def find(x):
    if groups[x] == x:
        return x
    return find(groups[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x>y:
        x, y = y, x
    groups[y] = x

for test_case in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]
    graph.sort(key=lambda x:x[2])
    groups = list(range(V+1))

    answer = 0
    for n1, n2, w in graph:
        if not find(n1)==find(n2):
            union(n1, n2)
            answer += w
    
    print(f'#{test_case} {answer}')
