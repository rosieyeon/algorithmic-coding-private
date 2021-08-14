import sys
import pdb
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stops = list(map(int,input().split()))
    
    count=0  
    bus = K  # 현재 버스 위치
    last_stop = 0

    while bus < N:
        if bus in bus_stops:
            count += 1
            last_stop = bus  # 마지막에 정차한 정류장은 저장해두기
            bus += K
        else:
            bus -= 1
            if bus == last_stop: 
                # 마지막에 정착한 버스 정류장이랑 같아질 경우 운행 불가능이므로 0출력
                count = 0
                break
            
    print(f'#{tc} {count}')
