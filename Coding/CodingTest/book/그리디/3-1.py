n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]  # 6
second = data[1]  # 5


result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


# 더 좋은 풀이방법
# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m-count) * second  # 두 번째로 큰 수 더하기
print(result)
# 6+6+6+5+6+6+6+5 = 46
