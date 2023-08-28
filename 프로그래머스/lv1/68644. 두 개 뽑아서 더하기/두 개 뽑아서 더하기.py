def solution(numbers):
    answer = []
    num_length = len(numbers)
    for i in range(num_length-1):
        for j in range(i+1, num_length):
            if (numbers[i]+numbers[j]) not in answer:
                answer.append(numbers[i]+numbers[j])
    return sorted(answer)