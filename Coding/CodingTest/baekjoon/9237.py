n = int(input())
tree = list(map(int, input().split()))
tree.sort(reverse=True)
count = 1
result = 0
for i in range(n):
    if tree[i]+count > result:
        result = tree[i]+count
    count += 1

print(result+1)
