k = int(input())
num = []
save = 0
for _ in range(k):
    m = int(input())
    if m == 0:
        num.pop()
    else:
        num.append(m)

print(sum(num))
