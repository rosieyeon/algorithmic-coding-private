import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = sorted(list(map(int, input().split())))
    deq = deque(a)
    result = []

    # 가장 오른쪽 pop! append! 그리고 가장 왼쪽 pop! append!
    for i in range(5):
        result.append(deq.pop())
        result.append(deq.popleft())

    print(f'#{test_case}', *result)


