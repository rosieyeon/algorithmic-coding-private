import sys
import pdb
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    result = (max(a)-min(a))
    
    print(f'#{tc} {result}')
