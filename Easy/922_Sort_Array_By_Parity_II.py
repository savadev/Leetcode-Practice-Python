A = [4,2,5,7]


def sortArrayByParityII(A):
 #   A_sorted = [0]*len(A)

    A_sorted = [0 for i in range(len(A))]
    even = 0
    odd = 1
    for i in A:

        if i % 2 == 0:
            A_sorted[even] = i
            even += 2

        else:
            A_sorted[odd] = i
            odd += 2

    print(A_sorted)
    return A_sorted



sortArrayByParityII(A)