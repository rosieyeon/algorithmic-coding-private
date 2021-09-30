import sys
sys.stdin = open('input.txt')
import pdb

hex_num = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def hex_to_int(num_str):
    res_int = 0
    num_str = num_str[::-1]
    # pdb.set_trace()
    for i in range(len(num_str)):
        if num_str[i] in hex_num.keys():
            res_int += hex_num[num_str[i]] *(16**i) 
        else:
            res_int += int(num_str[i]) *(16**i)
    return res_int


def int_to_bin(num_int):
    res_bin = ''
    while num_int > 0:
        res_bin += str(num_int%2)
        num_int = num_int // 2
    if len(res_bin)%4:
        res_bin += '0'
    return res_bin[::-1]


for test_case in range(1, int(input())+1):
    N, hex_N = input().split()
    print(f'#{test_case}', int_to_bin(hex_to_int(hex_N)))
