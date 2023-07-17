def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].islower():
            if ord(s[i])+n <= ord('z'):
                answer += chr(ord(s[i])+n)
            else:
                m = ord(s[i])+n-ord('z')
                answer += chr(ord('a')+m-1)
                
        elif s[i].isupper():
            if ord(s[i])+n <= ord('Z'):
                answer += chr(ord(s[i])+n)
            else:
                m2 = ord(s[i])+n-ord('Z')
                answer += chr(ord('A')+m2-1)
                
        elif s[i] == ' ':
            answer += ' '
    return answer