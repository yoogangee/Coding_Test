import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    network[a][b] = network[b][a] = 1

visited = [0]*(n+1)
cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    cnt += 1
    for i in range(1, n+1):
        if network[start][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)

print(cnt-1)