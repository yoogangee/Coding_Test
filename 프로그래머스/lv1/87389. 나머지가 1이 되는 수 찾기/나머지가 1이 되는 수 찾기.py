def solution(n):
    '''
    메모리: 10.2 MB, 시간: 0.00 ms
    x=1
    while n%x!=1:
        x += 1
    return x
    '''
    return [x for x in range(1,n+1) if n%x==1][0]