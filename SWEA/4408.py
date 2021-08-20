import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    time_chk = [0 for _ in range(201)]    

    for room in rooms:
        room.sort()  # 항상 번호가 작은 룸에서 큰 룸으로 이동하도록 정렬
        room[0] = (room[0]+1) //2
        room[1] = (room[1]+1) //2
        for x in range(room[0], room[1]+1):
            time_chk[x] += 1

    print(f'#{test_case} {max(time_chk)}')