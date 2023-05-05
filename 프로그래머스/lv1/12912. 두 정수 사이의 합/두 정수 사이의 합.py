def solution(a, b):
    if a > b:
        a, b = b, a
    if a!=b:
        return sum(range(a,b+1))
    return a