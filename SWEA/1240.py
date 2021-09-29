import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 눈 아픈 0들 사이에서 암호코드를 빼내주자! 
    for row in arr:
        if '1' in row:
            code = row
            break
    
    # 문제에서 보면 0부터 9까지의 숫자를 0과 1로 나타냈을 때 항상 마지막은 1로 끝남
    # 따라서 암호 코드를 뒤집에서 가장 처음 1이 나오는 인덱스가 몇번인지 구해줌
    # 그리고 거기서부터 숫자 56개만 빼내서 찐 암호를 code에 다시 저장함
    idx = code[::-1].index('1') 
    code = code[M-idx-56:M-idx]
    
    numbers = ['00110', '01100', '01001', '11110', '10001', '11000', '10111', '11101', '11011', '00101']
    code_num = []
    cnt = 0
    tmp = 0

    for i in range(8):
        number = code[i*7+1:i*7+6]
        print(number)
        for j in range(10):
            if numbers[j] == number:
                code_num.append(j)
                # 숫자로 변경된 암호를 code_num에 추가해줄 때마다 cnt를 하나씩 업그레이드
                cnt += 1
                # 홀수번째 숫자는 곱하기 3해서 tmp에 더해주고
                if cnt%2:
                    tmp += code_num[cnt-1]*3
                # 짝수번째 숫자는 그냥 더해줌
                else:
                    tmp += code_num[cnt-1]

    # 총 더해진 tmp가 10의 배수이면 총합을 출력, 그게 아니면 0!
    print(f'#{test_case}', 0 if tmp%10 else sum(code_num))
    