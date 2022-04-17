n = int(input())
data = []
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    data.append((a, b))

data.sort(key=lambda x: x[0])

for i in data:
    print(i[0], i[1])
