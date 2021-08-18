import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    pascal = [[1]]

    for i in range(0, N-1):
        pascal_row = [1]
        for j in range(0, i):
            pascal_row.append(pascal[i][j] + pascal[i][j+1])
        pascal_row.append(1)
        pascal.append(pascal_row)

    print(f'#{test_case}')
    for x in pascal:
        print(*x)


