def solution(s):
    p = [n for n in s if n=='p' or n=='P']
    y = [m for m in s if m=='y' or m=='Y']
    return len(p) == len(y)
    # count 라이브러리 사용
    # return s.lower().count('p') == s.lower().count('y')