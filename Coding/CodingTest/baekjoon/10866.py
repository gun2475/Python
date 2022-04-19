import sys

N = int(input())
deck = []
for _ in range(N):
    str = sys.stdin.readline().split()
    if str[0] == 'push_front':
        deck.insert(0, str[1])
    elif str[0] == 'push_back':
        deck.append(str[1])
    elif str[0] == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif str[0] == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
    elif str[0] == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(0))
    elif str[0] == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(-1))
    elif str[0] == 'size':
        print(len(deck))
    elif str[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
