import sys
sys.stdin = open('input.txt')

#cost: 이전 달까지의 계산 결과, m은 현재 내가 보낼 결과
def calculate(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    calculate(cost + d*month[m], m+1)
    calculate(cost +m1, m+1)
    calculate(cost + m3, m+3)


for test_case in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    min_cost = y

    calculate(0,1)
    print(f'#{test_case} {min_cost}')