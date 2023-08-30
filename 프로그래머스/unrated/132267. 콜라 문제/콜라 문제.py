def solution(a, b, n):
    answer = 0
    get_coke = 0
    empty_coke = 0
    left_coke = 0
    check = ''
    
    while n >= a:
        empty_coke = (n//a)*a
        get_coke = empty_coke/a*b
        n = n - empty_coke + get_coke
        answer += get_coke
        
    return answer