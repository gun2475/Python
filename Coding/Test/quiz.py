quiz = (['3+2', 5, 3], ['5/2', 2, 5], ['10-2', 8, 3],
        ['2^4', 16, 5], ['4/2', 2, 3])
ansCount = 0
wrongCount = 0
totalScore = 0

for item in quiz:
    print('문제:', item[0])
    ans = int(input('정답 입력:'))
    if ans == item[1]:
        ansCount += 1
        totalScore += item[2]
    else:
        wrongCount += 1
print('정답개수:', ansCount)
print('오답개수:', wrongCount)
print('점수:', totalScore)
