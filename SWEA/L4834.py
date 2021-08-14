import sys
import pdb
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    nums = set(a)  # 중복되는 숫자를 없애고 nums 리스트에 넣어줌
    result = {}  # 각각의 숫자가 몇개씩 적혀있는지 저장할 딕셔너리
    max_nums = []  # 가장 많은 숫자카드의 번호를 여기에 저장할 예정

    for num in nums:
        result[num] = 0  # 딕셔너리 안에 a의 값을 key 값으로 넣어줌
    for ai in a:
        result[ai] += 1  # 각각의 key값에 해당하는 숫자카드가 몇 개 있는지 value에 넣어줌

    max_nums = [key for m in [max(result.values())] for key,val in result.items() if val == m]
    # result 안에 value의 값이 가장 큰 key값을 저장해줌
    print(f'#{tc} {max(max_nums)} {result[max(max_nums)]}')
    # max_nums 안에서 가장 높은 키값을 출력! 그리고 그에 해당하는 value값도 출력!
