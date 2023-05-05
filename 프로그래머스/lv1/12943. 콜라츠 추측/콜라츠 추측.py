def solution(num):
    if num == 1:
        return 0
    for i in range(500):
        if num%2 == 0:
            num /= 2
        elif num != 1 and num%2 == 1:
            num = num*3+1
        else:
            return i
    return -1