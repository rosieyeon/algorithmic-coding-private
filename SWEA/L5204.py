import sys
sys.stdin = open('input.txt')

def merge_sort(numbers):
    n = len(numbers)
    if n < 2: return numbers
    
    left = merge_sort(numbers[:n//2])
    right = merge_sort(numbers[n//2:])
    return merge(left, right)


def merge(left, right):
    global cnt
    answer = []
    n_left, n_right = 0, 0

    if left[-1] > right[-1]:
        cnt += 1

    while n_left != len(left) and n_right != len(right):
        if left[n_left] <= right[n_right]:
            answer.append(left[n_left])
            n_left += 1
        else:
            answer.append(right[n_right])
            n_right += 1
    
    answer += left[n_left:]
    answer += right[n_right:]

    return answer


for test_case in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    print(f'#{test_case}', merge_sort(numbers)[N//2], cnt)
