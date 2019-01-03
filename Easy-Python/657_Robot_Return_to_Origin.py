from collections import Counter

moves = "UD"


def judgeCircle(moves):
    i = 0
    j = 0

    for move in moves:
        if move == 'U':
            j += 1
        elif move == 'D':
            j -= 1
        elif move == 'R':
            i += 1
        else:
            i -= 1

    if i == 0 and j == 0:
        return True

    return False


def judgeCircle_2(moves):
    if moves == '':
        return True
    count = Counter(moves)
    
    if count['L'] == count['R'] and count['U'] == count['D']:
        return True
    else:
        return False

judgeCircle_2(moves)