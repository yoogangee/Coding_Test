def solution(n):
    answer = 0
    temp = ''
    while n>0:
        temp = str(n%3) + temp
        n //= 3
    ex = 1
    for i in temp:
        answer += ex*int(i)
        ex *= 3
    return answer