import sys
sys.stdin = open('input.txt')

for test_case in range(1, 10+1):
    N = int(input())
    building = list(map(int, input().split()))

    i = 2
    count = 0
    while i < N-2:
        l_max = max(building[i-1], building[i-2])  # 왼쪽 두개 중 max 찾기
        r_max = max(building[i+1], building[i+2])  # 오른쪽 두개 중 max 찾기
        if building[i] > l_max and building[i] > r_max:
            # 그 중에서 내가 제일 크면 조망권 좋은 세대수를 계산해주기
            res = min(building[i] - l_max, building[i] - r_max) 
            count += res
            i += 3  # 일단 내가 조망권 가지면 오른쪽 두개는 볼 필요도 없이 gg
        else: i += 1  # 내 조망권이 gg면 바로 옆부터 다시 살펴 봅시다.
    print(f'#{test_case} {count}')

