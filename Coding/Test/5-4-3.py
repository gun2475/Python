f = open('E:\Python\Coding\Test\sales.txt', 'r')

file = f.read()
sales = file.split()
sum = 0
for i in sales:
    sum += int(i)
f.close()
avg = int(sum/len(sales))

f = open('E:\Python\Coding\Test\summary.txt', 'w', encoding='utf-8')
f.write('총매출 = ')
f.write(str(sum))
f.write('\n')
f.write('평균 일매출 = ')
f.write(str(avg))
f.close()
