from collections import deque

n, k = map(int, input().split())
array = deque([i+1 for i in range(n)])
sorT = []

while array:
    array.rotate(-(k-1))
    sorT.append(array.popleft())

print('<', end='')

for i in range(len(sorT)):
    n = sorT[i]
    if i == len(sorT)-1:
        print(f'{n}>')
    else:
        print(f'{n}, ', end='')
