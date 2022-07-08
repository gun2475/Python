def alternate(A):
    for v in A:
        v_is_largest = True
        for x in A:
            if v < x:
                v_is_largest = False
                break
        if v_is_largest:
            return v
    return None


A = [3, 4, 5, 1, 0, 10, 3, 5, 3]
print(alternate(A))
