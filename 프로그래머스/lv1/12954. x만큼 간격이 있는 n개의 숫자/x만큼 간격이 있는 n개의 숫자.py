def solution(x, n):
    if x != 0: 
        return [int(i) for i in range(x,x+x*n,x)]
    else:
        return [x for i in range(n)]