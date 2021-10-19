import sys
sys.stdin = open('input.txt')

import heapq

DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

def dijkstra(): 
    distance = [[int(1e9)]*N for _ in range(N)]
    distance[0][0] = 0

    heap = []
    heapq.heappush(heap, [0,0,0])
    while heap:
        cost, r, c = heapq.heappop(heap)
        if distance[r][c] < cost:
            continue

        for dr, dc in DIRECTIONS:
            nr, nc = dr+r, dc+c
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] > arr[r][c]:
                    extra_fee = arr[nr][nc] - arr[r][c]
                    n_cost = extra_fee + cost + 1
                else: n_cost = cost + 1
                if distance[nr][nc] > n_cost:
                    distance[nr][nc] = n_cost
                    heapq.heappush(heap, [n_cost, nr, nc])
    return distance[-1][-1]


for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {dijkstra()}')
    