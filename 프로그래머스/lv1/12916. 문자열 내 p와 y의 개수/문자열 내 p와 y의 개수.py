def solution(s):
    p = [n for n in s if n=='p' or n=='P']
    y = [m for m in s if m=='y' or m=='Y']
    if len(p) == len(y):
        return True
    else:
        return False