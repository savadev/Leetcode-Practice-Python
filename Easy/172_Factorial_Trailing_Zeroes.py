class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        while n > 0:
            product = product * n
            n -= 1

        num = 0
        reverse = str(product)[::-1]
        for item in reverse:
            if int(item) == 0:
                num += 1
            else:
                return num

    def trailingZeroes_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n > 0:
            n //= 5
            c += n
        return c

