def base26(w):
    val = 0
    for ch in w.lower():
        next_digit = ord(ch)-ord('a')
        val = 26*val + next_digit
    return val


print(base26('a'))
print(base26('ab'))
print(base26('abc'))
print(base26('abcd'))
print(base26('abcde'))
print(base26('abcdef'))
print(base26('abcdefg'))
print(base26('abcdefh'))
