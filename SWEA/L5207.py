import sys
sys.stdin = open('input.txt')

def binary_search(arr, key):
    low, high = 0, len(arr)-1
    flag, before = 'flag', 0
    
    while low <= high and not flag == before:
        mid = (low + high)//2
        before = flag

        if arr[mid] == key:
            return True

        elif arr[mid] > key:
            high = mid - 1
            flag = -1

        else:
            low = mid + 1
            flag = 1

    return False

for test_case in range(1, int(input())+1):
    N , M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for num in B:
        if binary_search(A, num):
            cnt += 1

    print(f'#{test_case} {cnt}')
