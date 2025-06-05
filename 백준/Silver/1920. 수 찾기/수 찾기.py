N = int(input())
n_array = set(map(int, input().split()))
M = int(input())
m_array = map(int, input().split())

for i in m_array:
    print(1 if i in n_array else 0)

