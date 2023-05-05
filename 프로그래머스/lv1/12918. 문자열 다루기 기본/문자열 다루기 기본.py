def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if '0'>i or '9'<i:
                return False
        return True
    return False
