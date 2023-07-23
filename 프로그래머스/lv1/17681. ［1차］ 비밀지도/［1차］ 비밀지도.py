def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1Wall = format(arr1[i], 'b').zfill(n)
        arr2Wall = format(arr2[i], 'b').zfill(n)
        
        Wall = ""
        for j in range(n):
            if arr1Wall[j] == '1' or arr2Wall[j] == '1':
                Wall += '#'
            else:
                Wall += ' '
                
        answer.append(Wall)
        
    return answer