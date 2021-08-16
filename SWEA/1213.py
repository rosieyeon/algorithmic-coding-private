import sys
sys.stdin = open('input.txt')

for test_case in range(1, 10+1):
    input()
    target = input()
    sentences = input()

    print(f'#{test_case} {sentences.count(target)}')