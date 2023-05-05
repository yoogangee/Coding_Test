def solution(a, b):
    if a > b:
        a, b = b, a
    if a!=b:
        return sum([i for i in range(a,b+1)])
    return a