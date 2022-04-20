students = ['홍길동', '김철수', '이영희', '강힘찬', '이여리', '박차오름']
print(students)

print('가나다순 정렬\n')
students.sort()
print(students)

print('이영희 전학감\n')
students.remove('이영희')
print(students)
print(len(students))

print('제일 앞 2명 선별\n')
print(students[:2])

print('이병규 전학 옴\n')
students.append('이병규')
print(students)

print('역순으로 바꿈')
students.reverse()
print(students)

print('이여리 이름 바꿈')
ind = students.index('이여리')
students[ind] = '이예리'
print(students)
