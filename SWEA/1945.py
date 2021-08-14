import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    alp = [0]*5  # 결과 a, b, c, d, e의 값을 저장해줄 리스트
    nums_list = [2, 3, 5, 7, 11]
    for i in range(len(nums_list)):
        x=0
        while not x:  #나머지(x)가 1이 될 경우 반복문 종료
            x = N % nums_list[i]
            if x: break
            else:
                N = N/nums_list[i]
                alp[i] +=1
    print(f'#{tc}', *alp)
