# 백준 14502 연수실

from collections import deque
import copy
from itertools import combinations

# bfs - 바이러스 퍼짐
def bfs(i):
    lab2 = copy.deepcopy(lab)
    q = deque()
    sol = 0
    for t in range(len(i)):
        x, y = i[t]
        lab2[x][y] = 1
    for x in range(n):
        for y in range(m):
            if lab2[x][y] == 2:
                q.append([x, y])
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and lab2[nx][ny] == 0:
                lab2[nx][ny] = 2
                q.append([nx,ny])

    # 0 개수 세기
    for k in lab2:
        sol += k.count(0)
    return sol


n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dy,dx = [0,0,1,-1],[1,-1,0,0]
lst = []
check = [] #안전 구역 수 저장하는 리스트

# 빈칸 저장
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            lst.append([i,j])

# 조합 사용해 벽 3개
for i in combinations(lst, 3):
    check.append(bfs(i))
print(max(check))