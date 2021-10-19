import sys
sys.stdin = open('input.txt')

def partition(A, l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, left, right):
    if left < right:
        s = partition(A, left, right)
        quick_sort(A, left, s-1)
        quick_sort(A, s+1, right)


for test_case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quick_sort(arr, 0, len(arr)-1)
    print(f'#{test_case} {arr[N//2]}')