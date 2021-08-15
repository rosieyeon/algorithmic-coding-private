import sys
import pdb
sys.stdin = open('input.txt')

# 리스트를 90도 회전시킬 함수
def rotated(a):
    n = len(a)
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = a[i][j]
    return result

# 리스트 안에서 단어를 넣을 수 있는 위치를 찾기
def count_wordspaces (puzzle_list):
    cnt = 0
    puzzle = [[0]*(len(puzzle_list)+2) for _ in range(len(puzzle_list))]

    # 입력 받은 퍼즐의 가로 부분 양 옆에 0을 추가해준다
    for y in range(len(puzzle_list)):
        for x in range(1, len(puzzle_list)+1):
            puzzle[y][x] = puzzle_list[y][x-1]

    # 연속된 k개의 합이 k이고, 그 양옆까지 다 더했을 때도 합이 k일 경우만 +1
    for row in puzzle:
        for i in range(1, len(puzzle[0])-1):
            if sum(row[i:i+K]) == K and sum(row[i-1:i+K+1]) ==K:
                cnt += 1
    return cnt

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    rot_puzzle = rotated(puzzle)

    # 퍼즐의 가로부분 계산
    count = count_wordspaces(puzzle)

    # 퍼즐의 세로부분 계산 (90도 회전해서 계산함)
    count += count_wordspaces(rot_puzzle)

    print(f'#{test_case} {count}')
