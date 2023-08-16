def solution(strings, n):
    answer = []
    strings = sorted(strings)
    
    for i in range(len(strings)):
        for j in range(len(strings)-i-1):
            if ord(strings[j][n]) > ord(strings[j+1][n]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
                
    return strings