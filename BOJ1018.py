import sys
n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
check1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
check2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
answer = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        sub1 = 0
        sub2 = 0
        for h in range(8):
            for w in range(8):
                if check1[h][w] != board[i + h][j + w]:
                    sub1 += 1
                if check2[h][w] != board[i + h][j + w]:
                    sub2 += 1
        sub = min(sub1, sub2)
        answer = min(answer, sub)
print(answer)
