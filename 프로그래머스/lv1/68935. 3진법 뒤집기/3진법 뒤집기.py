def solution(n):
    temp = ''
    answer = 0
    while n>0:
        temp = str(n%3) + temp
        n //= 3
        
    ex = 1
    for i in temp:
        answer += ex*int(i)
        ex *= 3
    return answer

# int('진법 문자열', 해당진법숫자) -> 10진수로 바꿔준다!
'''
def solution(n):
    temp = ''
    while > 0:
        temp += str(n%3)
        n //= 3
    return int(temp,3)
'''
