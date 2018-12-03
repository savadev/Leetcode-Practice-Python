A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]


def flipAndInvertImage(A):
    for a in range(0,len(A)):
        A[a].reverse()
        A[a] = [1 if i == 0 else 0 for i in A[a]]
    print(A)

def flipAndInvertImage_2(A):
    for a in range(0, len(A)):
        A[a] = A[a][::-1]
        A[a] = [1 if i == 0 else 0 for i in A[a]]
    print(A)



flipAndInvertImage_2(A)