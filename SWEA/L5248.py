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
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    groups = list(range(N+1))

    for i in range(0, 2*M, 2):
        union(numbers[i], numbers[i+1])

    result = set()
    for i in range(1, N+1):
        result.add(find(i))
    
    print(f'#{test_case} {len(result)}')
        