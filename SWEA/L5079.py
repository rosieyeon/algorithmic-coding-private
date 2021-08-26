import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(f'#{test_case} {numbers[M%N]}')