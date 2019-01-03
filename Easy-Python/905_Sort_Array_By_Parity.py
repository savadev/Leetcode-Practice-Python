A = [3,1,2,4]

def sortArrayByParity(A):
    list1 = []
    list2 = []
    for i in A:
        if i % 2 == 0:
            list1.append(i)
        else:
            list2.append(i)

    return list1 + list2


def sortArrayByParity_2(A):
    A.sort(key=lambda x: x % 2)
    return A


sortArrayByParity(A)