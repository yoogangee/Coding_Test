def solution(s):
    a = list(s)
    tmp = 0
    for i in range(len(s)):
        if a[i] == ' ':
            tmp = i-1
        else:
            if (i-tmp)%2==0:
                a[i] = a[i].upper()
            else:
                a[i] = a[i].lower()
                
    return ''.join(a)