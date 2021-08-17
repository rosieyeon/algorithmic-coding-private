import sys
sys.stdin = open('input.txt')

def check(row):
    for i in range(len(row)//2):
        if row[i]!=row[-i-1]:
            return False
    return True
   
for test_case in range(1, 10+1): 
    input()
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    result = 0

    for M in range(100, 0, -1):
        if result: break
        for row, row2 in zip(arr, arr2):
            if result : break
            for i in range(100-M+1):
                if check(row[i:i+M+1]) or check(row2[i:i+M+1]):
                    result = len(row[i:i+M+1])
                    print(f'#{test_case} {result}')
                    break
