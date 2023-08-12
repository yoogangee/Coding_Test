n, m = map(int, input().split())
select_card = list()

for i in range(n):
    line = [int(k) for k in input().split()]
    select_card.append(min(line))

print(max(select_card))