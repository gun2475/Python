from re import A


def add(a, b):
    return a+b


def addd(a, b):
    print('함수의 결과:', a+b)


a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()


print(add(3, 7))
addd(b=3, a=7)
print(a)

# 람다 표현식으로 구현한 add() 메소드
print((lambda a, b: a+b)(3, 7))
