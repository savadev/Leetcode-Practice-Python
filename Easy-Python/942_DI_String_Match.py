
S = "IDD"


def diStringMatch(S):
    left = 0
    right = len(S)
    A = []
    for s in S:
        if s == 'I':
            A.append(left)
            left += 1
        else:
            A.append(right)
            right -= 1
    print(A)
    return A + [left]

diStringMatch(S)



