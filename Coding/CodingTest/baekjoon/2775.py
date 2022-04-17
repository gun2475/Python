T = int(input())
sum = 0
for _ in range(T):
    k = int(input())
    n = int(input())
    case = [i+1 for i in range(n)]
    apart = []
    apart.append(case)
    for _ in range(k):
        room = []
        for j in range(n):
            if j == 0:
                room.append(1)
            else:
                for a in range(j+1):
                    sum += case[a]

                room.append(sum)
                sum = 0
        case = room[:]
        apart.append(room)
    print(apart[k][n-1])
