# 백준 33557 곱셈을 누가 이렇게 해 ㅋㅋ
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = input().rstrip().split()

    ab = int(a) * int(b)

    if len(a) < len(b):
        a,b = b, a.rjust(len(b), '1') #
    elif len(b) < len(a):
        b = b.rjust(len(a), '1')

    c = int(''.join([str(int(a) * int(b)) for a, b in zip(a, b)]))

    if ab == c:
        print(1)
    else:
        print(0)