'''
def stringSection(s,n):
    sectionList = list()
    for i in range(len(s)-n+1):
        temp = ''
        for j in range(n):
            temp += s[i+j]
        sectionList.append(int(temp))
    return sectionList
    
def solution(t, p):
    answer = 0
    n = len(p)
    list = stringSection(t, n)
    for i in list:
        if i <= int(p):
            answer += 1
    return answer
'''

def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer