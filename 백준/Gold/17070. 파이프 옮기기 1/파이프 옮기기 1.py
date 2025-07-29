# 백준 17070 파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        hor, ver, diag = 0, 0, 0
        if board[i][j] == 0 and (i, j) != (0, 1):
            # 가로로 파이프 밀렸을 때
            if j>=1:
                hor += (dp[i][j-1][0] + dp[i][j-1][2])
            # 세로로 파이프 밀렸을 때
            if i>=1:
                ver += (dp[i-1][j][1] + dp[i-1][j][2])
            # 대각선으로  파이프 밀렸을 때
            if i>=1 and j>=1:
                if board[i-1][j] != 1 and board[i][j-1] != 1:
                    diag += sum(dp[i-1][j-1])

            dp[i][j] = [hor, ver, diag]
        #print(dp)

print(sum(dp[-1][-1]))