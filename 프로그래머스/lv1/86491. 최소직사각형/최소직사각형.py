def solution(sizes): 
    '''
    for i in range(len(sizes)):
        sizes[i][0], sizes[i][1] = max(sizes[i][0], sizes[i][1]), min(sizes[i][0], sizes[i][1])
    max_width = max(sizes[n][0] for n in range(len(sizes)))
    max_height = max(sizes[m][1] for m in range(len(sizes)))
        
    return max_width * max_height
    '''
    return max(max(i) for i in sizes) * max(min(j) for j in sizes)