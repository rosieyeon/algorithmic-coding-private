import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    a = list(map(int, input().split()))
    result = []  # 인접한 M개의 숫자 합을 저장해줄 리스트 

    for i in range(N-M+1): 
        result.append(sum(a[i:i+M]))  # 더해준 애들 모두 저장저장
    
    print(f'#{tc} {max(result) - min(result)}')
        