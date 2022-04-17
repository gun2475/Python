from primePy import primes  # 파이썬 소수 구하는 모듈인데 백준에서 싫다고 한다.
a, b = map(int, input().split())
data = primes.between(a, b)

n_data = list(set(data))


for len in n_data:
    print(len)
