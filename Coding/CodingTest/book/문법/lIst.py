a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법1)
a = list()
print(a)

# 빈 리스트 선언 방법2)
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 변경
a[3] = 7
print(a)

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 파이썬 자료구조/알고리즘에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용함.

# N X M 크기의 2차원 리스트 초기화 (잘못된 방법) 채성이가 *은 파이썬에서 얕은 복사라고 한다.
n = 3
m = 4
array = [[0]*m]*n
print(array)

array[1][1] = 5
print(array)

a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입:  ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬:", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print('result : ', result)
