def solution(d, budget):
    arr = sorted(d)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > budget:
            return i
        elif sum == budget:
            return i+1
    return len(arr)            