n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)
count = 0
for arr in array:
    count += m//arr
    m %= arr

print(count)
