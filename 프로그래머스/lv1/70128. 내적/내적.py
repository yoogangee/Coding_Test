def solution(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))
    #return sum([x*y for x, y in zip(a,b)])