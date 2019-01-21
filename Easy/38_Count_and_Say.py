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







def countAndSay_2(n):
    dict = {1: "1"}
    if n == 1:
        return dict[1]

    i = 2

    while i <= n:
        print(i)
        output = ''
        previous = dict[i - 1][0]
        count = 1
        for j in range(1, len(dict[i - 1])):
            if dict[i - 1][j] == previous:
                count = count + 1
            else:
                output = output + str(count) + dict[i - 1][j-1]
                previous = dict[i - 1][j]
                count = 1

        output = output + str(count) + previous


        print(output)
        dict[i] = output
        print(dict)
        i += 1

    print(dict[n])
    return dict[n]

countAndSay_2(5)
