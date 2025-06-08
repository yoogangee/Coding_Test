# 백준 1946 신입사원

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    score = []
    # 성적 저장
    for _ in range(n):
        score.append(list(map(int, input().split())))
    
    score.sort()
    
    cnt = 1 #합격자 count
    top = 0 #비교 대상 중 면접 순위 가장 높은 것 저장
    for i in range(1, n):
        if score[top][1] > score[i][1]:
            cnt += 1
            top = i

    print(cnt, end='\n')