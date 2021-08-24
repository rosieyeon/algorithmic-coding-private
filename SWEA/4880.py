import sys
sys.stdin = open('input.txt')

def find_winner (x, y): 
    card_num1, card_num2 = cards[x-1], cards[y-1]
    if abs(card_num1 - card_num2) == 1:
        if card_num1 > card_num2: return x
        else: return y
    if abs(card_num1 - card_num2) == 2:
        if card_num1 > card_num2: return y
        else: return x
    if card_num1 == card_num2:
        return x

def play_game (start, end):
    if start == end:
        return start
    winner1 = play_game(start, (start+end)//2)
    winner2 = play_game((start+end)//2+1, end)

    return find_winner(winner1, winner2)
    
    
for test_case in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))

    print(f'#{test_case} {play_game(1, N)}')
    