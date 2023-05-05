def solution(absolutes, signs):
    list_len = len(absolutes)
    a = sum([absolutes[i] for i in range(list_len) if signs[i]])
    b = sum([absolutes[j] for j in range(list_len) if not signs[j]])
    return  a-b 