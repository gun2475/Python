for num in range(1, 100):
    first = num//10
    second = num % 10
    if first == 0:
        first = 1
    if second == 0:
        second = 1
    if(first % 3 == 0) and (second % 3 == 0):
        print(num, '박수짝짝\n')
    elif(first % 3 == 0 and second % 3 != 0) or (first % 3 != 0 and second % 3 == 0):
        print(num, '박수짝\n')
    else:
        print(num, '박수없음\n')
