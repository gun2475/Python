n, k = map(int, input().split())
array = [i+1 for i in range(n)]

for i in array:
    print(array.pop(k+i))
