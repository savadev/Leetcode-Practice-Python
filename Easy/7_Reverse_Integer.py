
x=-123


def reverse(x):
    print(x)

    if x >= 0:
        x = int(str(x)[::-1])
        print(x)
    else:
        num = str(x)[1:]
        print(num)
        num = num[::-1]
        x = int(num) * -1
        print(x)

    if x < -2 ** 31 or x > (2 ** 31) - 1:
        return 0

    print(x)
    return x


reverse(x)
