N = int(input())

m = 10001

arr = [0]*m
for i in range(N):
    arr[int(input())] += 1

for i in range(m):
    for j in range(arr[i]):
        print(i)
