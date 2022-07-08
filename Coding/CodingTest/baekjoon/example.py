N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

arr.sort()
# or
arr2 = sorted(arr)

print(arr)
print(arr2)
