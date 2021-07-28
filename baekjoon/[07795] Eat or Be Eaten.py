T = int(input())

for test_case in range(T):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()
    total = 0

    for num_a in A:
        first = 0
        last = len(B)-1
        
        while first <= last:
            mid = (first + last) // 2

            if B[mid] < num_a:
                first = mid + 1

            else:
                last = mid - 1

        total += first
    print(total)
