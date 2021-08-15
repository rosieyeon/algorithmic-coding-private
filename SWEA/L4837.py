import sys
sys.stdin = open('input.txt')

from itertools import combinations 

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    
    sub_sets = list(combinations(range(1, 13), N))

    cnt = 0 
    for sub_set in sub_sets:
        if sum(sub_set) == K:
             cnt += 1
    print(f'#{test_case} {cnt}')