
left = 1
right = 22


def selfDividingNumbers(left, right):
    num = []
    for number in range(int(left), int(right+1)):
        state = True

        for digit in str(number):
            if int(digit) == 0 or int(number) % int(digit) != 0:
                state = False
                break

        if state:
            num.append(number)

    print(num)
    return num



selfDividingNumbers(left, right)