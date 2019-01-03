
digits = [4,3,2,1]
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num_str = ''
    num_new = ''
    outs = []
    for digit in digits:
        num_str = num_str + str(digit)
        num_new = str(int(num_str)+1)

    for out in num_new:
        outs.append(int(out))
        print(int(outs))


plusOne(digits)