N = int(input())

arr = list(map(int, input().split()))

arr.sort()

time = 0
tmp = 0
for i in range(N):
    for j in range(i+1):
        tmp += arr[j]
    time += tmp
    tmp = 0


print(time)
