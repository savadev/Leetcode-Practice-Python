

import math

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    output = 1
    for i in range(1, int(n/2+1)):
        y = int(n-i*2) + i  # total digits
        output += int(math.factorial(y)/math.factorial(i)/math.factorial(y-i))
        print(output)


def climbStairs_2(n):
    fib = [0,1,2]

    if n == 1:
        return fib[1]
    if n == 2:
        return fib[2]

    for i in range(3,n+1):
        out = fib[i-2] + fib[i-1]
        fib.append(out)


    print(out)


climbStairs_2(5)