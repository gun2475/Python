# 데이터의 개수 입력
import sys
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n, m,. k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답판정가능
# 그래서 파이썬의 sys라이브러리에 정의되어 있는 sys.stdin.readline()함수를 이용함
sys.stdin.readline().rstrip()
# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

# 파이썬 3.6 이상의 버전부터 f-string 문법을 사용할 수 있다. 문자열 앞에 접두사 'f'을 붙임으로써 사용 가능함
# 단순히 중괄호({}) 안에 변수를 넣음으로써, 자료형의 변환 없이도 간단히 문자열과 정수를 함께 넣을 수 있다.
answer = 7
print(f"정답은 ({answer})입니다.")
