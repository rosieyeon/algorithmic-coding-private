import sys
sys.stdin = open('input.txt')

pattern = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9,
}

def bin_to_int(number):
    # 문제에서 숫자를 2진수 표기로 나타내는 방법에서, 왼쪽의 0을 모두 제거하고 생각해줌
    # 0: 1101, 1: 11001 ... -> 이런식으로 생각해주었음
    # 따라서 맨 왼쪽의 1의 개수, 중앙의 0의 개수, 맨 오른쪽의 1의  개수를 센 다음 그 비율을 통해 숫자를 알아내고자 함
    # 위의 pattern dictionary도 같은 맥락에서 만들어 주었음
    right1 = number.rstrip('1')  # 맨오른쪽 1 제거
    zero = right1.rstrip('0')  # 맨오른쪽 1, 0 제거
    left1 = zero.rstrip('1')  # 맨오른쪽 1, 0, 1 제거
    p3 = len(number) - len(right1)  # 맨오른쪽 1의 갯수
    p2 = len(right1) - len(zero)  # 중앙 0의 갯수
    p1 = len(zero) - len(left1)  # 왼쪽 1의 개수
    gcd = min(p1, p2, p3)  # 두께를 고려해줌 (최대공약수를 찾아서 나누어줄 예정)
    # p1, p2, p3의 최대공약수를 찾아서 나누어주면 비율을 알 수 있음
    # 이 문제에서 위의 pattern dictionary의 key값을 보면 전부 1을 포함하고 있는 걸 알 수 있음
    # 그래서 걍 p1, p2, p3의 최소값이 최대공약수가 되어버림
    res_bin = str(p1//gcd) + str(p2//gcd) + str(p3//gcd)  # e.g. '211'
    number = left1.rstrip('0')  # 숫자 하나를 해독했으면 이제 0을 지워줄거임
    # 위에서 언급했듯이 숫자를 2진수로 표기하는 과정에서 왼쪽 0은 모두 생략해주었기 때문에 0을 지워줘야함
    if res_bin in pattern.keys():
        # 함수를 리턴할 때 해독한 숫자, 해독한 숫자를 지운 암호코드를 둘다 가지고 나갈거임
        return str(pattern[res_bin]), number
    # 혹시 딕셔너리에 존재하지 않는 키를 가지는 경우 '#'을 중간에 넣어줌으로써
    # 나중에 암호 해독 후 전부 숫자인지 아닌지 판별해주고자 했는데
    # 이 문제에선 딱히 필요가 없는듯함. 있으나 없으나 답이 똑같이 출력됨 -> 항상 숫자가 나오긴 하는 모양
    else: return '#', number


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = []

    # 암호를 입력받을 때 양옆의 0은 모두 지워줬고, 동일한 row가 이미 존재하면 더이상 넣어주지 않아서 중복을 막음
    for _ in range(N):
        val = input().strip('0')
        if val and val not in arr:
            arr.append(val)


    # 16진수로 받은 암호 코드를 2진수로 바꿔주는 과정
    # 맨 오른쪽에 가끔씩 생성되는 0 모두 지워줬고
    # 앞에 생기는 0b도 지워버림
    bin_code = []
    for row in arr:
        h = '0x' + row
        b = bin(int(h, 16))[2:]
        bin_code.append(b.strip('0'))
    

    # 8자리 암호를 해독하고 검증하는 과정
    codes_list = []
    even, odd, res = 0, 0, 0
    for bin_num in bin_code:
        while bin_num:
            code = ''
            for i in range(8):
                new_bin_num = bin_num  # 해독한 숫자는 지워준 상태로 다시 해독하기 위함
                int_num, bin_num = bin_to_int(new_bin_num)
                code += int_num
            
            # 암호가 전부 숫자인지, 이미 이전에 해독한 암호인지 확인
            if code.isdigit and code not in codes_list:
                # 뒤에서부터 암호를 해독했기 때문에 암호의 순서가 반대로 되어 있음
                # 어차피 자릿수대로 더해주는 상황이라 다시 바꿔줄 필요 없어서
                # 짝수자리를 홀수로, 홀수자리를 짝수로 고려해줘서 계산
                odd = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7])
                even = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6])
                if not (odd*3 + even)%10:
                    # 검증을 통과하면 결과값에 더해주고, 리스트에도 추가해줘서 중복으로 더해지는 걸 막아주었음
                    res += (even + odd)
                    codes_list.append(code)
    print(f'#{test_case} {res}')
