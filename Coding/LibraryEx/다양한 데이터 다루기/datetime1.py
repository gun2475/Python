# 날짜를 계산하고 요일을 알려면? - datetime.date
import datetime
day1 = datetime.date(2022, 5, 15)
print(day1)
day2 = datetime.date(2022, 5, 20)
print(day2)

# day2에서 day1을 빼면 datetime.timedelta 객체가 반환되고 이 객체를 이용하면 두 날짜의 차이를 확인할 수 있다.
# datetime.datetime 객체
# datetime.date는 년, 월, 일로만 구성된 날짜 데이터이므로 시, 분, 초까지 포함한 일시 데이터를 생성하려면 다음과 같이 datetime.datetime을 사용해야 한다.
diff = day2 - day1
print(diff)
print(diff.days)

# 요일 판별하기 weekday()함수를 사용하여 5이면 토요일이다.
# 더 쉽게 보기 위해서는 isoweekday()함수를 사용하면 1이 월요일이다.
print(day1.weekday())
print(day1.isoweekday())
