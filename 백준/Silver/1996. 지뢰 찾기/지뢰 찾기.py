# 백준 1996 지뢰 찾기

n = int(input())
info = [list(map(str, input())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        cnt = 0
        if info[i][j] != '.':
            answer[i][j] = "*"

        else:
            # 위
            if i-1 >= 0:
                if info[i-1][j] != ".":
                    cnt += int(info[i-1][j])
                # 왼쪽 위
                if j-1 >= 0:
                    if info[i-1][j-1] != ".":
                        cnt += int(info[i-1][j-1])
                # 오른쪽 위
                if j+1 <= n-1:
                    if info[i-1][j+1] != ".":
                        cnt += int(info[i-1][j+1])
            
            # 아래 
            if i+1 <= n-1:
                if info[i+1][j] != ".":
                    cnt += int(info[i+1][j])
                # 왼쪽 아래
                if j-1 >= 0:
                    if info[i+1][j-1] != ".":
                        cnt += int(info[i+1][j-1])
                # 오른쪽 아래
                if j+1 <= n-1:
                    if info[i+1][j+1] != ".":
                        cnt += int(info[i+1][j+1])
                
            if j-1 >= 0:
                    if info[i][j-1] != ".":
                        cnt += int(info[i][j-1])
            
            if j+1 <= n-1:
                    if info[i][j+1] != ".":
                        cnt += int(info[i][j+1])
            
            if cnt >= 10:
                answer[i][j] = "M"
            else:
                answer[i][j] = cnt

for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()