def solution(absolutes, signs):
    list_len = len(absolutes)
    return sum([absolutes[i] for i in range(list_len) if signs[i]]) - sum([absolutes[j] for j in range(list_len) if not signs[j]])