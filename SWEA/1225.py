import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    input()
    password = list(map(int, input().split()))
    number = 1

    while number > 0:
        for i in range(1, 6):
            number = password.pop(0) - i
            if number <= 0 : 
                password.append(0)
                break
            password.append(number)

    print(f'#{test_case}', *password)
