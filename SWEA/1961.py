import sys
sys.stdin = open('input.txt')

def rotate_90(arr):
    rot_arr = list(zip(*arr[::-1]))
    return rot_arr

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = rotate_90(arr)
    arr180 = rotate_90(arr90)
    arr270 = rotate_90(arr180)

    print(f'#{test_case}')
    for row1, row2, row3 in zip(arr90, arr180, arr270):
        for x in (row1, row2, row3):
            print(*x, sep='', end=' ')
        print()
