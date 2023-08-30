def solution(food):
    answer = ''
    for i in range(1,len(food)):
        count = food[i]//2
        answer += str(i)*count
    reverse = answer[::-1]
    answer += "0"
    answer += reverse
    return answer