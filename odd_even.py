
def odd_even(A: list[int]) -> None:
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        print(next_even, next_odd)
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
        print(A)



# test cases
odd_even([1,3,4,7,8,10,12,13])

