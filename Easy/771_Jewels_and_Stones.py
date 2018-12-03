J = "aA"
S = "aAAbbbb"


def numjewelsinstones(J,S):
    c = 0
    for i in S:
        if i in J:
            c += 1
    return c



