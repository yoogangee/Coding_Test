answer = 0
n,m,k = map(int, input().split())
num_list = [int(n) for n in input().split()]

num_list = sorted(num_list, reverse=True)

while m>0:
    for i in range(k):
        answer += num_list[0]
        m -= 1
    if num_list[0] != num_list[1]:
        answer += num_list[1]
        m -= 1
    else:
        for i in range(k):
            answer += num_list[0]
            m -= 1

print(answer)
