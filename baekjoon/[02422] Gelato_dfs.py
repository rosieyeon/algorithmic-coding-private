import pdb

def dfs(idx, arr):
    if len(arr) == 3 :
        result.append(arr[:])
        return

    for i in range(idx, N):
        dfs(i+1, arr + [gelato[i]])
        

N, M = map(int, input().split())
gelato = list(range(1, N+1))
bad_flavor = [[0]*(N+1) for _ in range(N+1)]
result = []
cnt = 0

dfs(0, [])

for _ in range(M):
    a, b = map(int, input().split())
    bad_flavor[a][b], bad_flavor[b][a] = 1, 1

for ice in result:
    fv0, fv1, fv2 = ice[0], ice[1], ice[2]
    if bad_flavor[fv0][fv1] or bad_flavor[fv0][fv2] or bad_flavor[fv1][fv2]:
        continue
    cnt += 1

print(cnt)
