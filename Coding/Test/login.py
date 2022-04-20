passwd = 'abcd'
count = 0
while True:
    if count >= 5:
        print('로그인 실패! 횟수초과')
        break
    inpass = input('암호 입력하세요')
    if inpass != passwd:
        print('암호 다시 입력')
        count += 1
    elif inpass == passwd:
        print('로그인 됐습니다')
        break
