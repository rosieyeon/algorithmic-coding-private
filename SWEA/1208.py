import sys
sys.stdin = open('input.txt')

for tc in range(1, 10+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        top_idx = boxes.index(max(boxes))
        btm_idx = boxes.index(min(boxes))
        boxes[top_idx] -= 1
        boxes[btm_idx] += 1
        
    print(f'#{tc} {max(boxes)-min(boxes)}')
