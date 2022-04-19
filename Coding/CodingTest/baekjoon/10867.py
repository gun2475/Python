import sys
N = int(sys.stdin.readline())

m = 10001

arr = [0]*m
for i in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(m):
    for j in range(arr[i]):
        print(i)
