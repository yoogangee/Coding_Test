# 백준 9020 골드바흐의 추측
import sys
input=sys.stdin.readline

def is_Prime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    lt, rt = n/2, n/2

    while lt>0:
        if is_Prime(lt) and is_Prime(rt):
            print(int(lt), int(rt))
            break
        else:
            lt -= 1
            rt += 1