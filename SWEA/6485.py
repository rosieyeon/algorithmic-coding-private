import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    buses = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    
    stations = [0 for _ in range(5000)]
    res = []

    for a,b in buses:
        for i in range(a, b+1):
            stations[i-1] += 1
    
    for x in C:
        res.append(stations[x-1])
    print(f'#{test_case}', *res)