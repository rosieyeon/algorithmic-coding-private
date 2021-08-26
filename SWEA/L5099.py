import sys
import pdb
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))  # 치즈의 양을 input으로 받아줌
    oven_none = []

    # pizza 리스트에 [피자번호, 치즈양]을 담아줌
    # ex) [[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]
    pizza = [[i+1, cheese[i]] for i in range(M)]

    idx = 0  # 넣어줄 피자 번호를 세어주기 위해 선언함
    oven = []
    for i in range(N):
        # 오븐 안에 피자를 넣어줌! [피자번호, 치즈양]을 넣어줬음
        # ex) [[1, 7], [2, 2], [3, 6]]
        oven.append([pizza[i][0], pizza[i][1]])
        idx += 1  # 피자를 넣을 떄마다 idx+1를 해주면서 나중에 넣을 피자의 인덱스를 계산하도록 해주었음

    cnt = 0  # 화덕에서 나온 피자의 수를 카운트해줄 거임
    while cnt < M-1:  #오븐 안에 피자가 하나만 남을때까지 돌릴거임
        for i in range(len(oven)):
            # 오븐을 돌면서 치즈의 양을 반으로 줄여주자!
            oven[i][1] //= 2
            if oven[i][1] == 0:  # 만약 치즈양이 0이라면
                if idx < M:  # 피자 인덱스가 M보다 작다는 가정하에 피자를 넣어준다
                    oven[i] = pizza[idx]
                    idx += 1  # 피자를 넣어주었으므로 피자 인덱스는 +1을 해준다
                    cnt += 1  # 피자를 빼주었으므로 카운트
                elif oven[i][0]:
                    # 피자 인덱스가 M을 넘는다면 더이상 넣어줄 피자가 없다는 뜻이다
                    # 그래서 이 때의 오븐 안의 피자값 [피자번호, 치즈양] 의 피자번호를 0으로 만들었고
                    # 화덕에서 피자를 뻈으므로 cnt +1
                    if cnt >= M-1: break
                    oven[i][0] = 0  
                    cnt += 1

    for x in oven:
        if x[0]:
            print(f'#{test_case} {x[0]}')
  
