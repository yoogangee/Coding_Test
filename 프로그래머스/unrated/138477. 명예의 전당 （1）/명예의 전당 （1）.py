def solution(k, score):
    answer = []
    rank = []
    if k > len(score):
        for i in range(len(score)):
            rank.append(score[i])
            rank.sort()
            answer.append(rank[0])
            
    else:
        for i in range(k):
            rank.append(score[i])
            rank.sort()
            answer.append(rank[0])

        for j in range(k,len(score)):
            if score[j] > rank[0]:
                rank[0] = score[j]
                rank.sort()
            answer.append(rank[0])
    return answer