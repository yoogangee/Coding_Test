def solution(array, commands):
    answer = []
    for ijk in commands:
        temp = sorted(array[ijk[0]-1:ijk[1]])
        answer.append(temp[ijk[2]-1])
    return answer