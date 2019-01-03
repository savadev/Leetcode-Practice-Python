x = 1
y = 56


def hammingDistance(x, y):
    return bin(x ^ y).count('1')

hammingDistance(x, y)

