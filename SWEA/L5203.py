import sys
sys.stdin = open('input.txt')
import pdb

def is_babygin(player, number):
    if player[number] == 3:
        return True  
    for i in range(len(player)-2):
        if player[i] >= 1 and player[i+1] >= 1 and player[i+2] >=1:
            return True
    return False


for test_case in range(1, int(input())+1):
    numbers = list(map(int, input().split()))

    player1 = [0]*10
    player2 = [0]*10
    winner = 0

    for i in range(len(numbers)):
        # pdb.set_trace()
        if i%2:
            player2[numbers[i]] += 1
            if is_babygin(player2, numbers[i]):
                winner = 2
                break
        else:
            player1[numbers[i]] += 1
            if is_babygin(player1, numbers[i]):
                winner = 1
                break
    print(f'#{test_case} {winner}')
