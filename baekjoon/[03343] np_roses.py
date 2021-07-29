import sys
import math
import numpy as np

input = lambda: sys.stdin.readline().rstrip()

N, A, B, C, D = map(int, input().split())

def compare(a, b, c, d):
    if (a/b) > (c/d):
        return a, b, c, d
    else:
        return c, d, a, b

an, bn, cn, dn = compare(A, B, C, D)

max_num = math.ceil(N/an)
flower_shop1 = np.arange(max_num+1)

p1 = flower_shop1 *bn
p_an = flower_shop1 * an


p2 = np.ceil((N - p_an)/cn) *dn
p2_real = np.clip(p2,0, max(p2))

total = p1 + p2_real

print(int(min(total)))