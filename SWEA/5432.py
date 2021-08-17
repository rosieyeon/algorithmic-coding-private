import sys
import time
sys.stdin = open('input.txt')

T = int(input())

start = time.time()
for test_case in range(1, T+1):
    brackets = input()
    iron_bar = 0
    cnt_cut = 0

    for i in range(len(brackets)):
        if brackets[i] == '(':
            iron_bar += 1
        elif brackets[i] == ')':
            if brackets[i-1] == '(': 
                iron_bar -= 1
                cnt_cut += iron_bar
            else:  
                iron_bar -= 1
                cnt_cut += 1

    print(f'#{test_case} {cnt_cut}')
    print(time.time()-start)