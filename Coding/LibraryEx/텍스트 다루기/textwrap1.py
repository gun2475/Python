import textwrap

# textwrap.shorten() 함수는 매개변수 width로 전달한 길이만큼 문자열을 줄여 표시한다.
print(textwrap.shorten("Life is short, you need python", width=15))

# 한글 문자열도 마찬가지지만 한글 1문자를 길이2가 아닌 1로 계산한다는 점을 생각해야한다.
# 축약 표시 [...] 을 ...으로 변경하고 싶다면 다음처럼 매개변수 placeholder을 이용해야한다.
print(textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15, placeholder='...'))
