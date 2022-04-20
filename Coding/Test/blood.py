bloods = []
for i in range(10):
    print('헌혈해 주셔서 감사합니다\n')
    print('혈액형 입력하세요')
    bloods.append(input('A,B,O,AB:'))

atype = 0
btype = 0
otype = 0
abtype = 0
for i in range(10):
    if bloods[i] == 'A':
        atype += 1
    elif bloods[i] == 'B':
        btype += 1
    elif bloods[i] == 'O':
        otype += 1
    else:
        abtype += 1
print('A형', atype)
print('B형', btype)
print('O형', otype)
print('AB형', abtype)
