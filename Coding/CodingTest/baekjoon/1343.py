Board = list(map(str, input()))

count = 0
srtIndex = 0
desIndex = 0
chk = 0
for i in range(len(Board)):
    if Board[i] == 'X':
        count += 1
        desIndex += 1
    elif Board[i] == '.':
        count = 0
        srtIndex += 1
        desIndex += 1
    if count == 2:
        if i+1 < len(Board):
            if Board[i+1] != 'X':
                for j in range(count):
                    Board[srtIndex+j] = 'B'
                count = 0
                srtIndex += 2
        else:
            for j in range(count):
                Board[srtIndex+j] = 'B'
            count = 0
            srtIndex += 2
    elif count == 4:
        for j in range(count):
            Board[srtIndex+j] = 'A'
        count = 0
        srtIndex += 4
    elif count == 1:
        if len(Board) == 1:
            chk += 1
    elif count == 3:
        if i+1 < len(Board):
            if Board[i+1] != 'X':
                chk += 1
        elif len(Board) == 3:
            chk += 1
        elif i+1 == len(Board):
            chk += 1

if chk > 0:
    print(-1)
else:
    for i in range(len(Board)):
        print(Board[i], end='')

# 위는 내가 짠 알고리즘 백준에서 틀렸다고 한다. 까다롭네요

text = input()
text = text.replace('XXXX', 'AAAA')
text = text.replace('XX', 'BB')

if 'X' in text:
    print('-1')
else:
    print(text)

# 인터넷 보고 배웠는데 킹받네요
