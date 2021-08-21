import sys
sys.stdin = open('input.txt')
from pprint import pprint

def make_sudoku_sqr (sudoku):
    sudoku_sqr = []
    cnt = 0
    for row in range(9):
        if row%3: 
            for i in range(3):
                sudoku_sqr[cnt+i] += sudoku[row][i*3:(i+1)*3]
        else:
            if sudoku_sqr: cnt+=3
            for j in range(3):
                sudoku_sqr.append(sudoku[row][j*3:(j+1)*3])
    return sudoku_sqr

def chk_sudoku (arr):
    numbers = list(range(1, 10))
    for row in arr:
        x = sorted(row)
        if x != numbers:
            return False
    return True

for test_case in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sudoku_90 = list(zip(*sudoku[::-1]))  # 90도 회전된 스도쿠
    sudoku_sqr = make_sudoku_sqr(sudoku)  # 3x3 크기의 정사각형 스도쿠 리스트

    if chk_sudoku(sudoku) and chk_sudoku(sudoku_90) and chk_sudoku(sudoku_sqr):
        result = True
    else: result = False

    print(f'#{test_case}', 1 if result else 0)