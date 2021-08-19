import sys
sys.stdin = open('input.txt')

def dp(n):
    if n < 2:
        return 1
    return dp(n-1) + 2*dp(n-2)

for test_case in range(1, int(input())+1):
    N = int(input())
    
    print(f'#{test_case} {dp(N/10)}')
