import sys

N = int(input())
queue = []

for _ in range(N):
    str = sys.stdin.readline().split()

    if str[0] == 'push':
        queue.append(str[1])
    elif str[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif str[0] == 'size':
        print(len(queue))
    elif str[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif str[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
