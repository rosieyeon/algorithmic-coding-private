import pdb

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
cars = list(map(int, input().split()))

def get_children_numb (numb, cars):
    total = 0
    for car in cars:
        total += numb//car
    return total

if N - M < 0:
    print(N)
else:
    first, last = 0, N * max(cars)
    while first <= last:
        mid = (first + last) // 2
        ch_numb = get_children_numb(mid, cars)
        if ch_numb >= N - M:
            last = mid - 1
            time = mid
        else:
            first = mid + 1
    
    ans = M + get_children_numb(time-1, cars)
    for i in range(M):
        if time % cars[i] == 0:
            ans += 1
            
        if N - ans == 0 :
            print(i+1)
            break
