import sys
sys.stdin = open('input.txt')

T = int(input())

def binary_search (end, target): 
    start = 1
    cnt = 0 

    while start <= end :
        mid = (start + end) // 2
        cnt += 1
        if target == mid:
            return cnt
        elif mid < target :
            start = mid
        elif mid > target:
            end = mid
            
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    a = binary_search(P, Pa)
    b = binary_search(P, Pb)

    if a > b:
        print(f'#{test_case} B')
    elif a < b:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')


