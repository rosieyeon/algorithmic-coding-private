import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    red = []  # 빨간색으로 칠해진 인덱스 값을 모아줄 리스트
    blue = []  # 파란색으로 칠해진 인덱스 값을 모아줄 리스트
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 빨간색일 경우 red에 저장저장
        if color == 1:
            for row in range(r1, r2+1):
                for col in range(c1, c2+1):
                    red.append([row,col])
        # 파란색일 경우 blue에 저장저장
        else :
            for row in range(r1, r2+1):
                for col in range(c1, c2+1):
                    blue.append([row,col])

    # red의 리스트를 돌면서 blue와 겹치는 부분이 있다면 +1
    for x in red:
        if x in blue:
            cnt += 1
    print(f'#{test_case} {cnt}')

