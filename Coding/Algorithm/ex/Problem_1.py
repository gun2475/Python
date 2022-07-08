def print_n(n):
    i = 0
    sum = 0
    while(i <= n):
        sum += i
        i += 1
    print(sum)

if __name__ == '__main__':
    input_n = input("n을 입력하세요 : ")
    print_n(int(input_n))
