members = {}
while True:
    select = int(input('\n1.회원가입 2.프로그램 종료'))
    if select == 1:
        iid = input('아이디 입력')
        pw = input('비밀번호 입력')
        members[iid] = pw
    elif select == 2:
        for key in members.keys():
            print(key, '\t', members[key])
        break
