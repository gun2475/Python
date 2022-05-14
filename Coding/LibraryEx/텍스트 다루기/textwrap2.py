import textwrap
# textwrap.wrap()은 긴 문자열을 원하는 길이로 줄 바꿈(wrapping)할 때 사용하는 함수이다.

long_text = 'Life is too short, you need python. ' * 10
print(long_text)

result = textwrap.wrap(long_text, width=70)
# 첫번째 단계로 textwrap.wrap()함수는 긴 문자열을 width 길이만큼 자르고 이를 리스트로 만들어 반환한다.
print(result)

# 두번째 단계로 이를 하나의 문자열로 표시하고자 다음과 같이 join() 함수로 문자열 사이에 줄 바꿈 문자(\n)을 넣어 하나로 합친 다음 출력한다.
print('\n'.join(result))

# 참고로 textwrap.fill() 함수를 사용하면 이 과정을 한번으로 줄일수 있다.
print(textwrap.fill(long_text, width=70))
