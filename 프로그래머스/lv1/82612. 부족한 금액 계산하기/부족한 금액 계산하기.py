def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += price*(i+1)
    if sum <= money:
        return 0
    else:
        return sum-money