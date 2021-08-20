import sys
import pdb
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    text = [list(input()) for _ in range(5)]
    count = 0

    print(f'#{test_case}', end=' ')
    while count < 5:
        count = 0
        for row in range(len(text)):
            if text[row]:
                print(text[row][0], end='')
                text[row].pop(0)
            else: count += 1
    print()
    