A = [[1,2,3],
     [4,5,6]]


def transpose(A):
    # learn how to create a new array
    A_trans = [([0] * (len(A))) for i in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            A_trans[i][j] = A[j][i]




transpose(A)
