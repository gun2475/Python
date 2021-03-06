# 파이썬 표준 라이브러리에서 중요한 라이브러리 6가지
# 1. 내장 함수: print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다.
#   파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.
import math
from collections import Counter
from collections import deque
from bisect import bisect_left, bisect_right
import heapq
from itertools import combinations_with_replacement
from itertools import product
from itertools import combinations
from itertools import permutations
result = sum([1, 2, 3, 4, 5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3+5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)],
                key=lambda x: x[1], reverse=True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(data)
# 2. itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다.
#   순열과 조합 라이브러리를 제공한다.

data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)
data = ['A', 'B', 'C']
result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(
    data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)
# 3. heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


def heapsort2(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# 4. bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# 5. collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
# 6. math : 필수적인 수학적 기능을 제공하는 라이브러리이다.
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련함수 부터 파이(pi)와 같은 상수를 포함하고 있다.
print(math.factorial(5))  # 5 팩토리얼을 출력

print(math.sqrt(7))  # 7의 제곱근을 출력

print(math.gcd(21, 14))

print(math.pi)  # 파이(pi) 출력
print(math.e)  # 자연상수 e 출력
