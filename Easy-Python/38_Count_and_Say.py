n = 7


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    next = '1'

    for i in range(1,n):
        next = count_digit(next)

    return next

def count_digit(digits):

    count = 0
    previous = digits[0]
    seq_new = ''

    for digit in digits:

        if digit == previous:
            count += 1
        else:

            seq_new += str(count) + previous
            previous = digit
            count = 1
    seq_new += str(count) + previous

    print(seq_new)

    return seq_new




countAndSay(n)