import sys
sys.stdin = open('input.txt')

# 사다리의 가로를 x, 세로를 y로 설정

def find_route(x, y, ladder):
    # y는 올라가는 것만 하면 되므로 98부터 쭉 올라가도록 설정
    for ny in reversed(range(1,y)):

        # 왼쪽으로 쭈욱 이동!
        if x and ladder[ny][x-1]:
            while x and ladder[ny][x-1]: x-=1

        # 오른쪽으로 쭈욱 이동!
        elif x<y and ladder[ny][x+1]:
            while x<y and ladder[ny][x+1]: x+=1
    return x
  
for test_case in range(1, 10+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점의 위치를 찾아주자. 위치 찾으면 시간단축 위해 break하고 나오기
    for j in range(100):
        if ladder[99][j] == 2:
            x = j
            break
    
    print(f'#{test_case} {find_route(x, 99, ladder)}')
