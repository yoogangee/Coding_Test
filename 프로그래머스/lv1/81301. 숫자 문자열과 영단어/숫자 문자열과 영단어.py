def solution(s):
    answer = ''
    num_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    i=0
    temp = ''
    while i<len(s):
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
            temp += s[i]
            i += 1
            if temp in num_dict:
                answer += num_dict[temp]
                temp = ''
                
        else:
            answer += s[i]
            i += 1
            
    return int(answer)