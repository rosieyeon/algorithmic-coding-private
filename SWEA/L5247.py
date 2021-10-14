import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs_cal(n, m):
    q = deque([n])
    while q:
        num = q.popleft()
        if num == m:
            return visited[num]
        
        for next_num in (num+1, num-1, num*2, num-10):
            if 0<next_num<=1000000 and not visited[next_num]:
                visited[next_num] = visited[num] + 1
                q.append(next_num)

for test_case in range(1, int(input())+1):
    N, M = map(int,input().split())
    visited = [0]*1000001

    print(f'#{test_case} {bfs_cal(N,M)}')