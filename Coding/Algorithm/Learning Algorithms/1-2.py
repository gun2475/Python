def largest(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max


A = [3, 4, 5, 1, 0, 10, 3, 5, 3]
print(largest(A))
