import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    input().split()
    nums_list = list(input().split())

    # 외계 행성에서 쓰는 숫자를 리스트로 정리해주자!
    alien_nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = ''

    # 외계 행성 숫자 리스트를 돌면서, 이와 겹치는 아이가 인풋에 있으면 결과값에 str 추가!
    # 몇 개나 추가할 지는 count를 이용하기
    for i in range(len(alien_nums)):
        result += (alien_nums[i] + ' ') * nums_list.count(alien_nums[i])
    
    print(f'#{test_case}\n{result}')
