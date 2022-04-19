N = int(input())
data = [[0 for i in range(2)]for j in range(N)]

for i in range(N):
    data[i][0], data[i][1] = input().split()
for i in range(N):
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

data.sort(key=lambda i: (i[0], i[1]))

for i, j in data:
    print(i, j)
