
n = int(input())
data = []
for _ in range(n):
    data.append(input())

n_data = list(set(data))
n_data.sort()
n_data.sort(key=len)


for len in n_data:
    answer = ''.join(len)
    print(answer)
