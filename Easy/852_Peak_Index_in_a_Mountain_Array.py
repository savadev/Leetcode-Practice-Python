A = [0,2,1,0]


def peakIndexInMountainArray(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            break
    print(i)
    return i

peakIndexInMountainArray(A)

