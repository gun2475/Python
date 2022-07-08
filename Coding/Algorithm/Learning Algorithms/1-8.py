def is_palindrome1(w):
    return w[::-1] == w


def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]

    return True


def is_palindrome_letters_only(s):
    """
    문자열에 알파벳이 아닌 문자가 포함된 경우에도 Palindrome을 확인합니다.
    대소문자를 무시합니다.
    python 3.3에서 도입된 casefold() 메서드는 다음과 같을 수 있습니다.
    lower()로 변환하는 이 오래된 메서드 대신 사용됩니다.
    """
    i = 0
    j = hi = len(s) - 1
    while i < j:
        # This type of logic appears in partition.
        # Find alpha characters and compare
        while not s[i].isalpha():
            i += 1
            if i == hi:
                break
        while not s[j].isalpha():
            j -= 1
            if j == 0:
                break

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True


a = 'A man, a plan, a canal. Panama!'
print(is_palindrome1(a))
print(is_palindrome2(a))
print(is_palindrome_letters_only(a))
