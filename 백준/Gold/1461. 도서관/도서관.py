# 백준 1461 도서관
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

negative, positive = [], []
for book in books:
    if book > 0: positive.append(book)
    else: negative.append(book)

positive.sort(reverse=True)
negative.sort()

distance = []
len_p = len(positive)
for i in range(len_p//m):
    distance.append(abs(positive[i*m]))
if len_p%m != 0:
    distance.append(abs(positive[len_p//m*m]))

len_n = len(negative)
for i in range(len_n//m):
    distance.append(abs(negative[i*m]))
if len_n%m != 0:
    distance.append(abs(negative[len_n//m*m]))

distance.sort()
max_distance = distance.pop()

print(max_distance+sum(distance)*2)
