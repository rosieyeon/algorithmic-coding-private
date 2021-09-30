import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = float(input())

    cnt = 0
    res = ''
    while cnt < 13:
        if N == 0: break
        N *= 2
        cnt += 1
        if N >= 1:
            res += '1'
            N -= 1
        else:
            res += '0'
    
    print(f'#{test_case}', 'overflow' if N>0 else res)
        