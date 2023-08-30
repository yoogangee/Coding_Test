def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score = 0
        for word in photo[i]:
            if word in name:
                score += yearning[name.index(word)]
        answer.append(score)
    return answer